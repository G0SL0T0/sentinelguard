const ctx = document.getElementById('riskChart').getContext('2d');
new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
        datasets: [{
            label: 'Уровень риска',
            data: [65, 59, 80, 81, 56, 55, 40],
            borderColor: '#4CAF50',
            tension: 0.4,
            fill: true,
            backgroundColor: 'rgba(76, 175, 80, 0.1)'
        }]
    },
    options: {
        responsive: true,
        animations: {
            tension: {
                duration: 1000,
                easing: 'linear',
                from: 0.5,
                to: 0.4,
                loop: true
            }
        }
    }
});