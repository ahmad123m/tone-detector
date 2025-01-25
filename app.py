from flask import Flask, render_template, request, jsonify
from transformers import pipeline
import torch

app = Flask(__name__)

# Initialize text analyzer with proper config
text_analyzer = pipeline(
    "text-classification",
    model="joeddav/distilbert-base-uncased-go-emotions-student",
    top_k=None,
    device=-1  # Force CPU
)

# Verified emoji mapping
TONE_MAP = {
    'admiration': {'emoji': '🤩', 'color': '#FF69B4'},
    'amusement': {'emoji': '😄', 'color': '#FFD700'},
    'anger': {'emoji': '😡', 'color': '#FF0000'},
    'annoyance': {'emoji': '😒', 'color': '#FFA07A'},
    'approval': {'emoji': '👍', 'color': '#90EE90'},
    'caring': {'emoji': '❤️', 'color': '#FFB6C1'},
    'confusion': {'emoji': '😕', 'color': '#D3D3D3'},
    'curiosity': {'emoji': '🧐', 'color': '#ADD8E6'},
    'desire': {'emoji': '😍', 'color': '#FF1493'},
    'disappointment': {'emoji': '😞', 'color': '#A9A9A9'},
    'disapproval': {'emoji': '👎', 'color': '#CD5C5C'},
    'disgust': {'emoji': '🤢', 'color': '#6B8E23'},
    'embarrassment': {'emoji': '😳', 'color': '#FFB6C1'},
    'excitement': {'emoji': '🎉', 'color': '#FFD700'},
    'fear': {'emoji': '😨', 'color': '#4B0082'},
    'gratitude': {'emoji': '🙏', 'color': '#32CD32'},
    'grief': {'emoji': '😢', 'color': '#000080'},
    'joy': {'emoji': '😊', 'color': '#FFD700'},
    'love': {'emoji': '💖', 'color': '#FF69B4'},
    'nervousness': {'emoji': '😬', 'color': '#DAA520'},
    'optimism': {'emoji': '🌟', 'color': '#FFD700'},
    'pride': {'emoji': '🦚', 'color': '#800080'},
    'realization': {'emoji': '💡', 'color': '#FFFF00'},
    'relief': {'emoji': '😌', 'color': '#98FB98'},
    'remorse': {'emoji': '😔', 'color': '#778899'},
    'sadness': {'emoji': '😢', 'color': '#1E90FF'},
    'surprise': {'emoji': '😲', 'color': '#FFA500'},
    'neutral': {'emoji': '😐', 'color': '#808080'}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        text = request.json.get('text', '')[:512]  # Limit input length
        if not text.strip():
            return jsonify({'analysis': []})
        
        results = text_analyzer(text)[0]
        processed = []
        
        for item in results:
            if item['score'] > 0.1:  # Confidence threshold
                tone = TONE_MAP.get(item['label'].lower(), {'emoji': '❓', 'color': '#CCCCCC'})
                processed.append({
                    **tone,
                    'label': item['label'].capitalize(),
                    'score': item['score']
                })
        
        return jsonify({'analysis': sorted(processed, key=lambda x: x['score'], reverse=True)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)