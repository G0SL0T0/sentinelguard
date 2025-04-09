// Смена тем
document.getElementById('theme-toggle').addEventListener('click', () => {
    const theme = document.getElementById('theme');
    theme.href = theme.href.includes('dark') 
        ? '/static/css/main.css' 
        : '/static/css/dark-theme.css';
});

// Обрабатываемые действия
document.addEventListener('click', (e) => {
    if (e.target.classList.contains('action-btn')) {
        const ip = e.target.dataset.ip;
        if (confirm(`Заблокировать хост ${ip}?`)) {
            fetch(`/api/host/${ip}/isolate`, { method: 'POST' })
                .then(() => {
                    e.target.textContent = 'Заблокирован';
                    e.target.disabled = true;
                });
        }
    }
});