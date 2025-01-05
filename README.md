# SkillBot 🤖 | Your Personalized Guide to Skills4Future

SkillNavigator is an intuitive chatbot that bridges the gap between curiosity and knowledge for the Skills4Future program. Whether you're seeking program details, guidance on how to apply, or learning about cutting-edge Green skills and AI technologies, SkillNavigator is here to assist you.

# ✨ Key Features

1. Understands and classifies user queries into specific intents using Logistic Regression.
2. Offers responses to questions about Skills4Future, from eligibility to advanced AI courses.
3. Engage in real-time, seamless chat through a sleek, web-based interface powered by Streamlit.
4. Keeps a log of your interactions for revisiting key insights or tracking improvement.

# 🔧 Technology Stack
Programming Language: Python
Libraries and Tools:
    nltk for text preprocessing (tokenization, stemming, stop-word removal).
    scikit-learn for intent classification using Logistic Regression and TF-IDF.    
    Streamlit for creating a dynamic and user-friendly interface.
    csv and datetime for logging interactions and monitoring chatbot performance.

# 🚀 How It Works
1. Preprocessing
SkillNavigator uses advanced preprocessing techniques to clean user inputs:

Converts text to lowercase.
Removes unhelpful stop words like “is” and “the.”
Reduces words to their root form (e.g., “running” → “run”).

2. Training
A dataset of intents, patterns, and responses is processed and vectorized using TF-IDF.
Logistic Regression is used to classify user inputs into predefined categories.

3. Response Generation
Based on the classified intent, the chatbot fetches and delivers a relevant response.
Handles out-of-scope queries with fallback responses to ensure user satisfaction.

4. User Interface
Streamlit powers a minimalistic and easy-to-navigate interface, making SkillNavigator accessible to everyone.

# 📬 Contact
Have questions or feedback? Let’s connect!

    Author: Ayaz Shaikh
    GitHub: AyazShaikh01
    Live Chatbot App: SkillNavigator