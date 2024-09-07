document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('predictionForm').addEventListener('submit', function(e) {
        const rainfall = document.getElementById('rainfall').value;
        const fertilizer = document.getElementById('fertilizer').value;
        const pesticide = document.getElementById('pesticide').value;

        if (isNaN(rainfall) || isNaN(fertilizer) || isNaN(pesticide)) {
            alert('Please enter valid numeric values for Rainfall, Fertilizer, and Pesticide.');
            e.preventDefault();
        }
    });
});
