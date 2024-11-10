var ctx = document.getElementById('radarChart');
var radarChart = new Chart(ctx, {
    type: 'radar',
    data: {
        labels: ['Экстраверсия', 'Нейротизм', 'Открытость', 'Добросовестность', 'Уступчивость'],
        datasets: [{
            label: 'Личностные характеристики',
            data: document.getElementById('radar_data').textContent,
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            r: {
                suggestedMin: 0,
                suggestedMax: 1
            }
        }
    }
});