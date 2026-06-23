from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the trained model when app starts
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

print("✅ Model loaded successfully!")

# Homepage
@app.route('/')
def home():
    return jsonify({
        "message": "Sentiment Analysis API is running!",
        "usage": "POST to /predict with {'text': 'your review here'}"
    })

# Prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Step 1: Get the data
    data = request.get_json()
    
    # Step 2: Validate input
    if not data or 'text' not in data:
        return jsonify({
            "error": "Please send JSON with 'text' field",
            "example": {"text": "This product is amazing"}
        }), 400
    
    text = data['text']
    
    # Step 3: Convert text to numbers
    X = vectorizer.transform([text])
    
    # Step 4: Get prediction
    prediction = model.predict(X)[0]
    
    # Step 5: Get confidence score
    probabilities = model.predict_proba(X)[0]
    confidence = round(float(probabilities.max()) * 100, 1)
    
    # Step 6: Return result
    return jsonify({
        "text": text,
        "sentiment": "positive" if prediction == 1 else "negative",
        "confidence": f"{confidence}%"
    })

if __name__ == '__main__':
    app.run(debug=True)