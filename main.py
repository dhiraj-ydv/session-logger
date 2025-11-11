import webview
import time
import threading
import json
import os
from datetime import datetime

CONFIG_FILE = 'config.json'

class StopwatchAPI:
    def __init__(self):
        self.running = False
        self.session_active = False
        self.start_time = 0
        self.elapsed_time = 0
        self.data_file = None
        self.sessions = []
        self.load_config()
        if self.data_file:
            self.load_sessions()

    def show_sessions_window(self):
        # The new window will share the same js_api instance
        webview.create_window(
            'Session History',
            'web/sessions.html',
            js_api=self,
            width=400,
            height=500
        )
    def load_config(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                self.data_file = config.get('db_path')

    def save_config(self):
        with open(CONFIG_FILE, 'w') as f:
            json.dump({'db_path': self.data_file}, f)

    def set_data_file(self, path):
        self.data_file = path
        self.save_config()
        self.load_sessions(path)
        return self.data_file

    def create_db(self):
        file_path = webview.windows[0].create_file_dialog(webview.FileDialog.SAVE, file_types=('JSON Files (*.json)',), save_filename='sessions.json')
        if file_path:
            if isinstance(file_path, tuple):
                self.data_file = file_path[0]
            else:
                self.data_file = file_path
            self.sessions = []
            self.save_session() # Create the file with empty sessions
            self.save_config()
            return self.data_file
        return None

    def open_db(self):
        file_paths = webview.windows[0].create_file_dialog(webview.FileDialog.OPEN, allow_multiple=False, file_types=('JSON Files (*.json)',))
        if file_paths:
            self.data_file = file_paths[0]
            self.load_sessions()
            self.save_config()
            return self.data_file
        return None

    # ---- Stopwatch core ----
    def toggle_stopwatch(self):
        if not self.running:
            # Start a new session
            self.running = True
            self.session_active = True
            self.start_time = time.time()
            self.elapsed_time = 0
            threading.Thread(target=self.update_time, daemon=True).start()
            return "running"
        else:
            # Stop and save the session
            self.running = False
            if self.data_file:
                self.save_session()
            
            self.elapsed_time = 0
            self.session_active = False
            return "stopped"

    def update_time(self):
        while self.running:
            self.elapsed_time = time.time() - self.start_time
            time.sleep(0.1)

    def get_time(self):
        return round(self.elapsed_time, 2)

    # ---- Data handling ----
    def load_sessions(self, path=None):
        file_path = path if path else self.data_file
        if file_path and os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    self.sessions = json.load(f)
                except json.JSONDecodeError:
                    self.sessions = [] # or handle corrupted file
        else:
            self.sessions = []

    def save_session(self):
        if not self.data_file:
            return

        end_time = time.time()
        duration = round(self.elapsed_time, 2)

        session_data = {
            "start": datetime.fromtimestamp(self.start_time).isoformat(),
            "end": datetime.fromtimestamp(end_time).isoformat(),
            "duration": duration
        }

        # Prevent appending duplicates if reset is hit multiple times
        if not any(s['start'] == session_data['start'] for s in self.sessions):
            self.sessions.append(session_data)

        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

        with open(self.data_file, 'w') as f:
            json.dump(self.sessions, f, indent=2)

        print(f"Saved session to {self.data_file}: {session_data}")
        return session_data

    def get_sessions(self):
        return self.sessions

    def get_current_data_file(self):
        return self.data_file




if __name__ == '__main__':
    api = StopwatchAPI()
    window = webview.create_window(
        'Stopwatch',
        'web/index.html',
        js_api=api,
        width=380,
        height=420,
        resizable=True
    )
    webview.start()
