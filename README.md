# Real-Time Tone Analyzer 🔍

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An AI-powered web application that analyzes text sentiment and emotions in real-time using Hugging Face's Transformers.

## Features ✨
- Real-time text analysis as you type
- 28 emotional tones detection
- Confidence percentage visualization
- Responsive modern UI
- Error handling and loading states

## Tech Stack 🛠️
- **Backend**: Python/Flask
- **AI Model**: `joeddav/distilbert-base-uncased-go-emotions-student`
- **Frontend**: HTML5, CSS3, JavaScript
- **Deployment**: Heroku

## Installation 💻
```bash
# Clone repository
git clone https://github.com/ahmad123m/tone-detector.git

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

## Usage 🚀
1. Type or paste text into the input box
2. Analysis appears automatically
3. Tones are displayed with emojis and confidence percentages

## Project Structure 📂
```
tone-detector/
├── app.py
├── requirements.txt
├── Procfile
├── static/
│   ├── style.css
│   ├── app.js
│   └── favicon.ico
└── templates/
    └── index.html
```

## License 📄
This project is licensed under the MIT License - see [LICENSE](LICENSE.txt) file for details

## Acknowledgments 🙏
- Hugging Face Transformers library
- Flask documentation
- Emoji data from Unicode Consortium
