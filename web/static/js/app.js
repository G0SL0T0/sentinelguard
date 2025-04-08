document.addEventListener('DOMContentLoaded', () => {
    
    fetch('/api/hosts')  // Хосты
        .then(response => response.json())
        .then(hosts => renderHosts(hosts));

    document.getElementById('theme-toggle').addEventListener('click', toggleTheme);
});

function renderHosts(hosts) {
    const table = document.querySelector('#hostsTable tbody');
    table.innerHTML = hosts.map(host => `
        <tr>
            <td><a href="/host/${host.ip}">${host.ip}</a></td>
            <td><span class="risk-badge" style="background: ${getRiskColor(host.risk)}">${host.risk}%</span></td>
            <td>${host.status}</td>
            <td><button onclick="isolateHost('${host.ip}')">Изолировать</button></td>
        </tr>
    `).join('');
}

function isolateHost(ip) {
    fetch(`/api/host/${ip}/isolate`, { method: 'POST' })
        .then(() => alert(`Хост ${ip} изолирован!`));
}

function getRiskColor(risk) {
    if (risk >= 80) return '#f44336';
    if (risk >= 50) return '#ff9800';
    return '#4CAF50';
}

function toggleTheme() {
    const theme = document.getElementById('theme');
    theme.href = theme.href.includes('dark') ? '/static/css/main.css' : '/static/css/dark-theme.css';
}