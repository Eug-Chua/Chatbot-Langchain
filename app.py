# Q&A Chatbot
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv
import os

# Take environment variables from .env file
load_dotenv()

import streamlit as st

## Function to load OpenAI model and get responses


def get_openai_response(question):
    try:
        # Initialize the chat model with API key, model name, and temperature
        chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),
                          model="gpt-4o-mini",
                          temperature=0.8)
        
        # Prepare the messages
        messages = [HumanMessage(content=question)]
        
        # Generate the response
        response = chat(messages)
        
        # Extract and return the content of the response
        return response.content
    except Exception as e:
        # Return the error message if an exception occurs
        return f"An error occurred: {e}"


## Initialize our Streamlit app
st.set_page_config(page_title="Q&A")

st.header("Langchain Application")

# Get user input from the text input widget
input_text = st.text_input("Input: ", key="input")

# Create a button to submit the question
submit = st.button("Ask question")

# If the submit button is clicked, get the response and display it
if submit:
    response = get_openai_response(input_text)
    st.subheader("The response is ")
    st.write(response)
