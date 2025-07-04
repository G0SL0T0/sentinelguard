// app.js
import Chart from 'chart.js/auto';

// charts.js
export function initCharts() {
    const ctx = document.getElementById('riskChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь'],
            datasets: [{
                label: 'Уровень риска',
                data: [65, 59, 80, 81, 56, 55],
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 2,
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
