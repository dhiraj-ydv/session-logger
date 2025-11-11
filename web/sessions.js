window.addEventListener('pywebviewready', () => {
  loadAndDisplaySessions();
});

async function loadAndDisplaySessions() {
  // Access the same JS API from the main window
  const sessions = await window.pywebview.api.get_sessions();
  const container = document.getElementById('history-container');

  if (!sessions || sessions.length === 0) {
    container.innerHTML = "<h3>No sessions found in the current database.</h3>";
    return;
  }

  // Sort sessions by start time, newest first
  sessions.sort((a, b) => new Date(b.start) - new Date(a.start));

  container.innerHTML = "<h3>Session History</h3>" +
    sessions.map(s => {
      const startTime = new Date(s.start);
      const date = startTime.toLocaleDateString();
      const time = startTime.toLocaleTimeString();
      return `
        <p>
          <strong>${date}</strong> at ${time} &rarr; <strong>${s.duration}s</strong>
        </p>
      `;
    }).join('');
}
