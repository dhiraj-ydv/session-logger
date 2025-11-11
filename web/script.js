let timerInterval = null;

async function updateTime() {
  const time = await window.pywebview.api.get_time();
  document.getElementById('time').innerText = time.toFixed(2);
}

// --- Button handlers ---
async function start() {
  const status = await window.pywebview.api.start();
  if (!timerInterval) {
    timerInterval = setInterval(updateTime, 100);
  }
  updateStatus(status);
}

async function stop() {
  const status = await window.pywebview.api.stop();
  clearInterval(timerInterval);
  timerInterval = null;
  updateStatus(status);
}

async function reset() {
  const status = await window.pywebview.api.reset();
  document.getElementById('time').innerText = '0.00';
  clearInterval(timerInterval);
  timerInterval = null;
  updateStatus(status);
  await showHistory();
}

// --- History display ---
async function showHistory() {
  const sessions = await window.pywebview.api.get_sessions();
  const container = document.getElementById('history');

  if (sessions.length === 0) {
    container.innerHTML = "<h3>No sessions yet</h3>";
    return;
  }

  container.innerHTML = "<h3>History</h3>" +
    sessions.map(s => `
      <p>🕒 ${s.start.slice(11,19)} → ${s.duration}s</p>
    `).join('');
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
