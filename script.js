const spamWords = {
    "win": 0.95,
    "prize": 0.9,
    "free": 0.85,
    "cash": 0.8,
    "offer": 0.85,
    "urgent": 0.9,
    "click": 0.85,
    "claim": 0.8,
    "buy now": 0.9,
    "guaranteed": 0.85,
    "limited time": 0.8,
    "congratulations": 0.9,
    "exclusive": 0.85,
    "won": 0.95,
    "girlfriend": 0.95,
    "Girlfriend": 0.95,
    "spam": 0.95
};

const hamWords = {
    "hello": 0.1,
    "meeting": 0.2,
    "project": 0.2,
    "schedule": 0.3,
    "team": 0.2,
    "update": 0.3,
    "invoice": 0.2,
    "report": 0.2,
    "thank you": 0.1,
    "regards": 0.1,
    "important": 0.2
};

function tokenize(text) {
    return text.toLowerCase().split(/\W+/).filter(word => word.length > 0);
}

function getWordProbabilities(text) {
    const tokens = tokenize(text);
    return tokens.map(token => {
        const spamProb = spamWords[token] || 0.5; // Neutral probability
        const hamProb = hamWords[token] || 0.5;   // Neutral probability
        return [spamProb, hamProb];
    });
}

function combineProbabilities(probabilities) {
    let spamProduct = 1, hamProduct = 1;
    probabilities.forEach(([spamProb, hamProb]) => {
        spamProduct *= spamProb;
        hamProduct *= hamProb;
    });
    return spamProduct / (spamProduct + hamProduct);
}

function checkSpam() {
    const message = document.getElementById("message").value;
    const wordProbabilities = getWordProbabilities(message);
    const spamScore = combineProbabilities(wordProbabilities);

    const resultElement = document.getElementById("result");
    if (spamScore > 0.6) {  // Adjusted threshold to 0.6 for better sensitivity
        resultElement.innerHTML = "This message is likely spam.";
        resultElement.style.color = "#D2122E";
    } else {
        resultElement.innerHTML = "This message is not spam.";
        resultElement.style.color = "green";
    }
}
document.getElementById('message').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault(); // Prevents the default action of the enter key (like adding a new line)
        checkSpam();
    }
});
