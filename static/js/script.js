async function predictDiabetes() {
    // Fetch input values
    const preg = parseFloat(document.getElementById('preg').value);
    // ... Fetch other input values ...

    // Make sure all values are provided
    if (isNaN(preg) || /* Check for other fields */) {
        alert('Please enter valid numeric values for all fields.');
        return;
    }

    // Make the prediction using a Python backend
    const prediction = await makePredictionFromBackend(preg, /* Other input values */);

    // Display the prediction result
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = `Prediction Result: ${prediction}`;
}

async function makePredictionFromBackend(preg, /* Other input values */) {
    // Use fetch or other methods to send the input data to the Python backend
    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            preg: preg,
            // ... Include other input fields ...
        }),
    });

    // Parse and return the prediction result
    const result = await response.json();
    return result.prediction;
}
