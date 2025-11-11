# 🕒 Stopwatch App  
*A Modern Desktop Stopwatch Built with Python, HTML/CSS & PyWebView*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyWebView](https://img.shields.io/badge/UI-PyWebView-0078d7.svg)](https://pywebview.flowrl.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

---

## 📖 Overview

**Stopwatch App** is a lightweight, modern desktop stopwatch built using **Python**, **HTML/CSS**, and **PyWebView**.  
It’s a perfect example of combining a **web-based frontend** with a **Python backend** to create a **native desktop experience** —  
without needing Electron, .NET, or C++.

---

## ✨ Features

✅ Start, Stop, and Reset stopwatch functionality  
✅ Pause and Resume — continues the same session (no duplicate entries)  
✅ Session history saved locally as JSON  
✅ Persistent data (your sessions stay saved even after restart)  
✅ Status indicator for **Running ⏱**, **Paused ⏸**, and **Saved 💾** states  
✅ Scrollable session history panel  
✅ Clean Windows 11–style Fluent UI look  
✅ 100% Python + HTML/CSS — no external JS frameworks required  

---

## 🧱 Project Structure

```
stopwatch-app/
│
├── main.py                # Python backend (logic, persistence)
├── data/
│   └── sessions.json      # Auto-created file for saved sessions
└── web/
    ├── index.html         # Frontend UI
    ├── style.css          # Styling (Fluent look)
    └── script.js          # JS logic for UI and PyWebView bridge
```

---

## ⚙️ Requirements

- **Python 3.8+**
- **pip** (Python package manager)

Install dependencies:

```bash
pip install pywebview
```

*(Optional for packaging as EXE)*  
```bash
pip install pyinstaller
```

---

## 🚀 How to Run the App

### 1️⃣ Clone this repository
```bash
git clone https://github.com/<ydvdhiraj>/stopwatch-app.git
cd stopwatch-app
```

### 2️⃣ Install dependencies
```bash
pip install pywebview
```

### 3️⃣ Run the app
```bash
python main.py
```

A native window will open — no browser required.

---

## 🖥️ How to Use

| Action | Description |
|--------|--------------|
| ▶️ **Start** | Starts or resumes the stopwatch |
| ⏸️ **Stop** | Pauses the stopwatch |
| 🔁 **Reset** | Stops and saves the current session |
| 🕒 **History** | Displays your saved sessions |

🧠 **Note:**  
- Stopping does *not* create a new session — it only pauses.  
- Pressing **Reset** saves the session permanently in `data/sessions.json`.  

---

## 💾 Data Storage

Your stopwatch sessions are saved automatically to:
```
data/sessions.json
```

Example data:
```json
[
  {
    "start": "2025-11-11T14:12:31.182433",
    "end": "2025-11-11T14:15:02.726530",
    "duration": 151.54
  },
  {
    "start": "2025-11-11T15:22:31.182433",
    "end": "2025-11-11T15:23:05.726530",
    "duration": 34.54
  }
]
```

---

## 🎨 User Interface

### 💻 Live Interface Preview

```
+-------------------------------------------+
|                ⏱ Stopwatch                |
|                                           |
|                   0.00                    |
|  [Start] [Stop] [Reset] [History]         |
|                                           |
|  🟢 Running / 🟠 Paused / 💾 Saved         |
|-------------------------------------------|
|  🕒 History                               |
|  14:12:31 → 151.54s                       |
|  15:22:31 → 34.54s                        |
+-------------------------------------------+
```

### 🪟 Fluent Design Feel
- White rounded container  
- Subtle shadows  
- Windows 11 accent blue (`#0078d7`)  
- Smooth animations on hover and buttons  

---

## 🧠 How It Works

**Architecture Diagram:**

```
┌──────────────────────────┐
│        Frontend          │
│ ──────────────────────── │
│ HTML / CSS / JavaScript  │
│ └── rendered in PyWebView│
└──────────▲───────────────┘
           │
           │ (bridge API)
           ▼
┌──────────────────────────┐
│         Backend           │
│ ───────────────────────── │
│ Python (main.py)          │
│ Stopwatch logic + storage │
│ JSON file for sessions    │
└───────────────────────────┘
```

**PyWebView** acts as a native app shell — it displays your web UI and directly connects  
your JavaScript (`script.js`) to Python methods via the `window.pywebview.api` bridge.

---

## 🏗️ Packaging into an Executable (Optional)

To create a `.exe` for Windows:

```bash
pyinstaller --onefile main.py
```

Your app will be packaged into `/dist/Stopwatch.exe`  
and can run on any Windows machine without Python installed.

---

## 🔮 Future Enhancements

🚧 Planned features:
- ⏱ Lap recording inside a running session  
- 🌓 Light/Dark mode toggle  
- 💾 Export sessions to CSV  
- 🗄 Move from JSON → SQLite database  
- ☁️ Optional cloud sync (OneDrive / Dropbox)  

---

## 🧑‍💻 Author

**[Dhiraj Yadav](https://github.com/ydvdhiraj**  
🌐 GitHub: [@ydvdhiraj](https://github.com/ydvdhiraj)  
📧 Contact: hello@dhiarjhq.com  

If you like this project, please ⭐ **star the repo** — it helps others discover it!

---

## 📜 License

```
MIT License © 2025 Dhiraj Yadav
```

---

⭐ **If this project helped you, don’t forget to give it a Star!**  
> Happy Coding — and enjoy your clean, modern Python stopwatch! 🕒
