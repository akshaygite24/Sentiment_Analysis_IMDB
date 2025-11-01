import joblib
from src.preprocessing import clean_code

try:
    model = joblib.load('models/sentiment_model.joblib')
    vectorizer = joblib.load('models/vectorizer.joblib')
except FileNotFoundError:
    raise Exception("Model or Vectorizer file not found. Please check models/ directory.")

def predict_sentiment(text):
    cleaned = clean_code(text)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    return "Positive" if prediction == 1 else "Negative"