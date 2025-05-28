from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import pandas as pd
import re
import joblib


# We'll use this function to replace numbers from the string
def preprocessor(text):
    return re.sub(r'[^a-z ]', '', text.lower())


data = pd.read_csv(
  'data/train.csv',
  names=['sentiment', 'title', 'review']
)

# Ignore reviews with a neutral sentiment
data = data[data.sentiment != 3]

# Access the corpus and target variables
X = data.review
y = data.sentiment.replace({1:'Negative', 2:'Negative', 4:'Positive', 5:'Positive'})

# train test splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)


# construct the pipeline with the procedural steps to
# process the data and cast predictions
pipe = Pipeline([
  ('vec', CountVectorizer(stop_words='english', min_df=1000, preprocessor=preprocessor)),
  ('tfid', TfidfTransformer()),
  ('lr', SGDClassifier(loss='log_loss'))
])

# fit the model to the data
model = pipe.fit(X_train, y_train)

joblib.dump(pipe, 'model/sentiment_model.pkl')
