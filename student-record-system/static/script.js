// ── SEARCH ──────────────────────────────────────────────────────────
async function searchStudents() {
  const query     = document.getElementById('searchInput').value.trim();
  const method    = document.querySelector('input[name="method"]:checked').value;
  const btn       = document.getElementById('searchBtn');
  const countEl   = document.getElementById('resultCount');
  const container = document.getElementById('resultsContainer');

  if (!query) {
    countEl.textContent = '⚠ Please enter a search term.';
    countEl.style.color = '#ff6b6b';
    return;
  }

  btn.textContent = 'Searching…'; btn.disabled = true;

  try {
    const res  = await fetch('/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query, method })
    });
    const data = await res.json();
    countEl.style.color = '#a8ff78';
    countEl.textContent =
      `✔ ${data.count} record(s) found using ${method === 'binary' ? '⚡ Binary' : '🔍 Linear'} Search`;
    container.innerHTML = data.results.length === 0
      ? `<div class="no-results">No students matched "<strong>${query}</strong>".</div>`
      : buildTable(data.results);
  } catch (err) {
    countEl.textContent = '✖ Error connecting to server.';
    countEl.style.color = '#ff6b6b';
  } finally {
    btn.textContent = 'Search'; btn.disabled = false;
  }
}

// ── SORT ────────────────────────────────────────────────────────────
async function sortStudents() {
  const algorithm = document.getElementById('sortAlgo').value;
  const key       = document.getElementById('sortKey').value;
  const reverse   = document.getElementById('sortOrder').value === 'desc';
  const btn       = document.getElementById('sortBtn');
  const countEl   = document.getElementById('sortCount');
  const container = document.getElementById('sortContainer');

  btn.textContent = 'Sorting…'; btn.disabled = true;

  try {
    const res  = await fetch('/sort', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ algorithm, key, reverse })
    });
    const data = await res.json();
    const names = { bubble: '🫧 Bubble Sort', quick: '⚡ Quick Sort', merge: '🔀 Merge Sort' };
    countEl.style.color = '#a8ff78';
    countEl.textContent = `✔ ${data.count} students sorted using ${names[algorithm]}`;
    container.innerHTML = buildTable(data.results);
  } catch (err) {
    countEl.textContent = '✖ Error connecting to server.';
    countEl.style.color = '#ff6b6b';
  } finally {
    btn.textContent = 'Sort'; btn.disabled = false;
  }
}

// ── TAB SWITCH ──────────────────────────────────────────────────────
function showTab(tab, el) {
  document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
  document.getElementById('tab-' + tab).classList.add('active');
  el.classList.add('active');
}

// ── BUILD TABLE ─────────────────────────────────────────────────────
function buildTable(students) {
  const rows = students.map(s => {
    const cgpaClass = s.cgpa >= 9 ? 'cgpa-high' : s.cgpa >= 8 ? 'cgpa-mid' : 'cgpa-low';
    return `
      <tr>
        <td><span class="badge-id">${s.id}</span></td>
        <td>${s.name}</td>
        <td>${s.dept}</td>
        <td class="${cgpaClass}">${s.cgpa.toFixed(1)}</td>
        <td>Year ${s.year}</td>
      </tr>`;
  }).join('');
  return `
    <table>
      <thead><tr>
        <th>STUDENT ID</th><th>NAME</th><th>DEPT</th><th>CGPA</th><th>YEAR</th>
      </tr></thead>
      <tbody>${rows}</tbody>
    </table>`;
}

// ── ENTER KEY ───────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('searchInput')
    .addEventListener('keypress', e => { if (e.key === 'Enter') searchStudents(); });
});