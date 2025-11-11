# 🕒 Stopwatch App  
*A Modern Desktop Stopwatch Built with Python, HTML/CSS & PyWebView*

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyWebView](https://img.shields.io/badge/UI-PyWebView-0078d7.svg)](https://pywebview.flowrl.com/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

---

## 📖 Overview

**Stopwatch App** is a lightweight, modern desktop stopwatch combining a **web-based frontend (HTML/CSS/JS)** with a **Python backend** using **PyWebView**. It offers a native desktop experience without complex frameworks.

---

## ✨ Features

✅ **Single Control Button:** Start and Stop the stopwatch with one intuitive button.
✅ **Automatic Session Saving:** Sessions are automatically saved to a user-selected JSON file when stopped.
✅ **Customizable Data Storage:** Choose where to save session data on the local file system.
✅ **Persistent Data:** Sessions are saved and loaded automatically from the last used database.
✅ **Session History Window:** View all saved sessions in a dedicated popup window.
✅ **Resizable Window:** The application window can be resized and maximized.
✅ **Clean UI:** Modern, clean interface with Fluent Design aesthetics.

---

## 🧱 Project Structure

```
stopwatch-app/
│
├── main.py                # Python backend (logic, persistence, API)
├── config.json            # Stores the path to the last used session database
└── web/
    ├── index.html         # Main application UI
    ├── style.css          # Styling for main UI and session window
    ├── script.js          # JS logic for main UI and PyWebView bridge
    ├── sessions.html      # UI for the session history popup window
    └── sessions.js        # JS logic for the session history popup
```

---

## ⚙️ Requirements

- **Python 3.8+**
- **pip** (Python package manager)

Install dependencies:

```bash
pip install pywebview
```

---

## 🚀 How to Run the App

### 1️⃣ Clone the repository
```bash
git clone https://github.com/dhiraj-ydv/stopwatch-app.git
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

1.  **Start/Stop:** Click the main button to start the stopwatch. Click it again to stop.
2.  **Create New Database:** Use the "Create DB" button in the top toolbar to select a location and name for a new session database (`.json` file).
3.  **Open Existing Database:** Use the "Open DB" button in the top toolbar to load an existing session database.
4.  **View Session History:** Click the "Sessions History" button in the footer to open a new window displaying all recorded sessions.
5.  **Current DB Path:** The path to the currently active session database is displayed in the footer.

---

## 💾 Data Storage

Stopwatch sessions are saved automatically to the selected or created `.json` file. The path to this file is remembered in `config.json`.

---

## 🎨 User Interface

### 🪟 Fluent Design Feel
- Clean, modern layout with a responsive design.
- White rounded container with subtle shadows.
- Windows 11 accent blue (`#0078d7`) for primary elements.
- Smooth animations on hover and buttons.

---

## 🧠 How It Works

**PyWebView** acts as a native app shell, displaying the web UI and connecting JavaScript to Python methods via the `window.pywebview.api` bridge. The Python backend handles all core logic, data persistence, and native OS interactions (like file dialogs and creating new windows).

---

## 🏗️ Packaging into an Executable (Optional)

To create a `.exe` for Windows:

```bash
pip install pyinstaller
pyinstaller --onefile main.py
```

The app will be packaged into `/dist/Stopwatch.exe` and can run on any Windows machine without a Python installation.

---

## 🔮 Future Enhancements

🚧 Planned features:  
- 🌓 Light/Dark mode toggle
- ☁️ Optional cloud sync

---

## 🧑‍💻 Author

**[Dhiraj Yadav](https://github.com/dhiraj-ydv)**  
🌐 GitHub: [@dhiraj-ydv](https://github.com/dhiraj-ydv)  
📧 Contact: hello@dhiarjhq.com  

If this project is helpful, please ⭐ **star the repo** — it helps others discover it!

---

⭐ **If this project is helpful, don’t forget to give it a Star!**  
> Happy Coding! 🕒
