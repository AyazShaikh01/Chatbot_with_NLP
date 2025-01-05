import os
import json
import nltk
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.preprocess import preprocess

# Load dataset
def load_data(file_path='data/dataset.json'):
    with open(file_path, 'r') as file:
        return json.load(file)

# Prepare data for training
def train_model(data):
    patterns, tags = [], []
    for intent in data:
        for pattern in intent['patterns']:
            patterns.append(preprocess(pattern))
            tags.append(intent['tag'])

# Convert text data to numerical features
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(patterns)

#Train the data
    model = LogisticRegression()
    model.fit(X, tags)
    return model, vectorizer


# Chatbot function
def get_response(input_text, model, vectorizer, data):
    processed_input = preprocess(input_text)
    input_vector = vectorizer.transform([processed_input])
    predicted_tag = model.predict(input_vector)[0]
    for intent in data:
        if intent['tag'] == predicted_tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I don't understand that."