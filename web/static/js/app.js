import { showSkeleton } from './animations.js';

// Фильтр таблицы
document.querySelector('.risk-filter').addEventListener('change', (e) => {
    const riskLevel = e.target.value;
    const rows = document.querySelectorAll('.log-table tbody tr');
    
    rows.forEach(row => {
        const riskCell = row.querySelector('.risk-level');
        if (!riskCell) return;
        
        const isHighRisk = riskCell.classList.contains('high');
        const isMediumRisk = riskCell.classList.contains('medium');
        
        if (riskLevel === 'all') {
            row.style.display = '';
        } else if (riskLevel === 'high' && isHighRisk) {
            row.style.display = '';
        } else if (riskLevel === 'medium' && isMediumRisk) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
});

// Сортировка по времени
document.querySelectorAll('.log-table th').forEach(header => {
    if (header.textContent === 'Время') {
        header.style.cursor = 'pointer';
        header.addEventListener('click', () => {
            const table = header.closest('table');
            const rows = Array.from(table.querySelectorAll('tbody tr'));
            
            rows.sort((a, b) => {
                const dateA = new Date(a.cells[0].textContent);
                const dateB = new Date(b.cells[0].textContent);
                return dateB - dateA;
            });
            
            table.querySelector('tbody').append(...rows);
        });
    }
});

window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    header.classList.toggle('scrolled', window.scrollY > 20);
});

showSkeleton();

// Анимация кнопок
document.querySelectorAll('button').forEach(btn => {
    btn.addEventListener('click', () => {
        gsap.to(btn, { scale: 0.95, duration: 0.2, yoyo: true, repeat: 1 });
    });
});