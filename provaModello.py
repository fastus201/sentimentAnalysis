import joblib
import re

def preprocessor(text):
    return re.sub(r'[^a-z ]', '', text.lower())

pipe = joblib.load('model/sentiment_model.pkl')
#Funziona solo in inglese
risultato = pipe.predict(["This product is very good, nice"])
print(risultato)