# SkillBot🌟 - Your Guide to the Skills4Future Program 
# Chatbot - Skills4Future Program

SkillBot, an interactive chatbot designed to provide accessible information and support about the Skills4Future program. Built using Natural Language Processing (NLP) techniques and machine learning models, SkillBot helps users explore program details, eligibility, application processes, and more.

# ✨ Key Features
1. Understands and classifies user queries into specific intents using Logistic Regression.
2. Quickly resolves common questions about the program, schedules, and opportunities.
3. Keeps a log of your interactions for revisiting key insights or tracking improvement.

# Tools and Technologies
Programming Language: Python
NLP Libraries:
    NLTK
    Scikit-learn (TF-IDF Vectorizer and Logistic Regression)
    Frontend Framework: Streamlit
Utilities:
csv for conversation logging
datetime for timestamps
json for file handling


# 🚀 How It Works
1. Preprocessing
SkillNavigator uses advanced preprocessing techniques to clean user inputs:
    Converts text to lowercase.
    Removes unhelpful stop words like “is” and “the.”
    Reduces words to their root form (e.g., “running” → “run”).

2. Training
A dataset of Tags, Patterns, and Responses is processed and vectorized using TF-IDF.
    Logistic Regression is used to classify user inputs into predefined categories.

3. Response Generation
Based on the classified intent, the chatbot fetches and delivers a relevant response.
Handles out-of-scope queries with fallback responses to ensure user satisfaction.

4. User Interface
Streamlit powers a minimalistic and easy-to-navigate interface, making SkillNavigator accessible to everyone.
