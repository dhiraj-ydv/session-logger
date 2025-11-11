import webview
import time
import threading
import json
import os
from datetime import datetime

DATA_FILE = 'data/sessions.json'

class StopwatchAPI:
    def __init__(self):
        self.running = False
        self.session_active = False
        self.start_time = 0
        self.elapsed_time = 0
        self.load_sessions()

    # ---- Stopwatch core ----
    def start(self):
        if not self.running:
            self.running = True
            if not self.session_active:
                # Start a new session
                self.session_active = True
                self.start_time = time.time()
                self.elapsed_time = 0
            else:
                # Resume existing session
                self.start_time = time.time() - self.elapsed_time
            threading.Thread(target=self.update_time, daemon=True).start()
            return "running"

    def stop(self):
        if self.running:
            self.running = False
            return "paused"
        return "stopped"

    def reset(self):
        if self.session_active:
            self.save_session()
            self.session_active = False
        self.running = False
        self.elapsed_time = 0
        return "saved"

    def update_time(self):
        while self.running:
            self.elapsed_time = time.time() - self.start_time
            time.sleep(0.1)

    def get_time(self):
        return round(self.elapsed_time, 2)

    # ---- Data handling ----
    def load_sessions(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                self.sessions = json.load(f)
        else:
            self.sessions = []

    def save_session(self):
        end_time = time.time()
        duration = round(self.elapsed_time, 2)

        session_data = {
            "start": datetime.fromtimestamp(self.start_time).isoformat(),
            "end": datetime.fromtimestamp(end_time).isoformat(),
            "duration": duration
        }

        self.sessions.append(session_data)
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

        with open(DATA_FILE, 'w') as f:
            json.dump(self.sessions, f, indent=2)

        print(f"Saved session: {session_data}")
        return session_data

    def get_sessions(self):
        return self.sessions


if __name__ == '__main__':
    api = StopwatchAPI()
    window = webview.create_window(
        'Stopwatch',
        'web/index.html',
        js_api=api,
        width=340,
        height=400,
        resizable=False
    )
    webview.start()
