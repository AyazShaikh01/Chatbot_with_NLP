from src.model import load_data, train_model, get_response
from datetime import datetime
import streamlit as st
import os
import csv
import streamlit as st
import nltk


nltk.download('punkt')
nltk.download('stopwords')

# Load data and train model
data = load_data()
model, vectorizer = train_model(data)


#setting up the UI
#File for Conversation History
csv_file = "history"

#checking if the CSV file exist of not.
if not os.path.exists(csv_file):
    with open(csv_file, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["User Input", "Chabot Response", "Time Stamp"])


#function TO log Conversation in CSV file
def log_csv(userInput, chatbotResponse):
    timestamp = datetime.now().strftime("%Y-%m-%d %H: %M: %S")
    with open(csv_file, mode = 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([userInput, chatbotResponse, timestamp])


#Sidebar
st.sidebar.title('Navigation')
option = st.sidebar.radio("GO TO: ", ["Home", "Conversation History", "About"])

if option == "Home":
    st.title("Chatbot - Skill4Future Program")
    st.write("I am Chatbot for Skill4Future!")

    #input Field
    user_input = st.text_input("You: ", key="input")

    #Response
    if user_input:
        response = get_response(user_input, model, vectorizer, data)
        log_csv(user_input, response)
        st.write(f"Bot:  {response}")

elif option == "Conversation History":
    st.title("History")
    if os.path.exists(csv_file):
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                st.write(f"**User:** {row[0]}")
                st.write(f"**Bot:** {row[1]}")
                st.write(f"**Timestamp:** {row[2]}")
                st.write("---")
    else:
        st.write("No Conversation History Available.")

elif option == "About":
    st.title("About")
    st.write("""
    This chatbot is designed to assist users with information about the Skills4Future program.
        It uses Natural Language Processing (NLP) techniques and machine learning to understand 
        and respond to user queries. Built with Python, Streamlit, and scikit-learn, this chatbot 
        demonstrates a simple yet effective implementation of conversational AI.
""")