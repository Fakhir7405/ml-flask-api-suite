# Sentiment Analysis API

An AI-powered REST API that analyzes text sentiment using Machine Learning.

## Tech Stack
- Python, Flask, scikit-learn
- Containerized with Docker

## Setup
pip install -r requirements.txt
python train.py
python app.py

## Usage
POST /predict
Content-Type: application/json
{"text": "Your review here"}

## Response
{"sentiment": "positive", "confidence": "94.2%"}