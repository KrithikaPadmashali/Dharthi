document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('.try-form');

  form.addEventListener('submit', async function (e) {
    e.preventDefault();

    // 1. Collect the 10 diameter values
    const inputs = form.querySelectorAll('input[type="number"]');
    const diameters = Array.from(inputs).map(input => parseFloat(input.value));

    // 2. Check if we have exactly 10 values
    if (diameters.length !== 10 || diameters.some(isNaN)) {
      alert("Please enter valid numbers for all 10 samples.");
      return;
    }

    // 3. Send POST request to Flask backend
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ diameters })
      });

      const result = await response.json();

      // 4. Handle errors from server
      if (result.error) {
        alert("Error: " + result.error);
        return;
      }

      // 5. Create result display
      const resultDiv = document.createElement('div');
      resultDiv.innerHTML = `
        <h3>Result:</h3>
        <p><strong>Soil Composition:</strong> ${result.composition.join("%, ")}%</p>
        <p><strong>Soil Type:</strong> ${result.soil_type}</p>
        <p><strong>Recommended Crops:</strong> ${result.recommended_crops.join(", ")}</p>
      `;
      resultDiv.style.fontSize = '1.2rem';
      resultDiv.style.marginTop = '30px';
      resultDiv.style.color = '#2d572c';

      // 6. Replace form with result + thank you message
      form.style.display = 'none';
      const thankYou = document.createElement('div');
      thankYou.textContent = 'Thanks for submitting!';
      thankYou.style.fontSize = '2rem';
      thankYou.style.color = '#ffb300';
      thankYou.style.textAlign = 'center';
      thankYou.style.marginTop = '40px';

      form.parentNode.appendChild(resultDiv);
      form.parentNode.appendChild(thankYou);
    } catch (err) {
      alert("Could not connect to the server. Make sure the Flask server is running.");
      console.error(err);
    }
  });
});
