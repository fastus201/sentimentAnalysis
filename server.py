from flask import Flask, request, jsonify, render_template
import joblib
import re

app = Flask(__name__)

def preprocessor(text):
    return re.sub(r'[^a-z ]', '', text.lower())

pipe = joblib.load('model/sentiment_model.pkl')

@app.route('/')
def home():
    return render_template('./index.html')

@app.route("/predict",methods=["POST"])
def predict():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'})

    # Usa il modello per predire probabilità
    probs = pipe.predict_proba([text])

    return jsonify({
        'probability': float(probs[0][1])
    })



if __name__ == '__main__':
    app.run(debug=True)