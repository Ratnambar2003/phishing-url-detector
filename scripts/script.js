function checkURL() {
    const urlInput = document.getElementById('urlInput').value;
    const resultDiv = document.getElementById('result');

    if (!urlInput) {
        showResult('Please enter a URL', 'unsafe');
        return;
    }

    fetch('/check', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: urlInput })
    })
    .then(response => response.json())
    .then(data => {
        const type = data.safe ? 'safe' : 'unsafe';
        showResult(data.message, type);
    })
    .catch(error => {
        showResult('Error checking URL. Try again later.', 'unsafe');
        console.error(error);
    });
}

function showResult(message, type) {
    const resultDiv = document.getElementById('result');
    resultDiv.style.display = 'block';
    resultDiv.className = 'result ' + type;
    resultDiv.textContent = message;
}
