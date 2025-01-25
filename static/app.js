const textInput = document.getElementById('text-input');
const resultsContainer = document.getElementById('results');
let analysisTimeout;

// Real-time analysis with 500ms debounce
textInput.addEventListener('input', () => {
    clearTimeout(analysisTimeout);
    analysisTimeout = setTimeout(performAnalysis, 500);
});

async function performAnalysis() {
    const text = textInput.value.trim();
    
    try {
        // Clear previous results
        resultsContainer.innerHTML = text ? 
            '<div class="loading"><i class="fas fa-spinner fa-spin"></i></div>' : 
            '<div class="empty-state"><i class="fas fa-comment-dots"></i><p>Your tone analysis will appear here</p></div>';
        
        if (!text) return;

        const response = await axios.post('/analyze', { text });
        
        if (response.data.error) {
            throw new Error(response.data.error);
        }

        updateResults(response.data.analysis);
    } catch (error) {
        resultsContainer.innerHTML = `
            <div class="error-message">
                <i class="fas fa-exclamation-triangle"></i>
                ${error.message}
            </div>
        `;
    }
}

function updateResults(analysis) {
    if (analysis.length === 0) {
        resultsContainer.innerHTML = `
            <div class="empty-state">
                <i class="fas fa-comment-slash"></i>
                <p>No strong tones detected</p>
            </div>
        `;
        return;
    }

    resultsContainer.innerHTML = analysis.map(tone => `
        <div class="tone-card" style="border-color: ${tone.color}">
            <div class="tone-header">
                <span class="tone-emoji">${tone.emoji}</span>
                <div>
                    <div class="tone-label">${tone.label}</div>
                </div>
            </div>
            <div class="tone-progress">
                <div class="tone-bar" style="width: ${tone.score * 100}%; background: ${tone.color}"></div>
            </div>
            <div class="tone-percent">${Math.round(tone.score * 100)}% confidence</div>
        </div>
    `).join('');
}