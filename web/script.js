let timerInterval = null;

window.addEventListener('pywebviewready', () => {
  updateFileDisplay();
});

async function updateTime() {
  const time = await window.pywebview.api.get_time();
  document.getElementById('time').innerText = time.toFixed(2);
}

async function toggleStopwatch() {
  const status = await window.pywebview.api.toggle_stopwatch();
  const toggleBtn = document.getElementById('toggle-btn');

  if (status === 'running') {
    toggleBtn.innerText = 'Stop';
    toggleBtn.classList.add('running');
    if (!timerInterval) {
      timerInterval = setInterval(updateTime, 100);
    }
  } else { // 'stopped'
    toggleBtn.innerText = 'Start';
    toggleBtn.classList.remove('running');
    clearInterval(timerInterval);
    timerInterval = null;
    document.getElementById('time').innerText = '0.00';
  }
  updateStatus(status);
}

async function openDb() {
    const filePath = await window.pywebview.api.open_db();
    if (filePath) {
        await updateFileDisplay();
    }
}

async function createDb() {
    const filePath = await window.pywebview.api.create_db();
    if (filePath) {
        await updateFileDisplay();
    }
}

async function updateFileDisplay() {
  const filePath = await window.pywebview.api.get_current_data_file();
  const fileDisplayEl = document.getElementById('file-display');
  if (filePath) {
    fileDisplayEl.innerText = filePath;
    fileDisplayEl.title = filePath;
  } else {
    fileDisplayEl.innerText = 'No DB Selected';
    fileDisplayEl.title = 'Create or open a database from the toolbar above.';
  }
}

async function showSessionsHistory() {
  await window.pywebview.api.show_sessions_window();
}

// --- Status indicator ---
function updateStatus(state) {
  const statusEl = document.getElementById('status');
  if (!statusEl) return;

  if (state === 'running') {
    statusEl.innerText = "⏱ Running...";
    statusEl.style.color = "green";
  } else if (state === 'paused') {
    statusEl.innerText = "⏸ Paused";
    statusEl.style.color = "orange";
  } else if (state === 'saved') {
    statusEl.innerText = "💾 Session saved";
    statusEl.style.color = "blue";
    setTimeout(() => { statusEl.innerText = ""; }, 2000);
  } else {
    statusEl.innerText = "";
  }
}
