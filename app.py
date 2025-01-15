import streamlit as st
from openai import OpenAI
from utils import response
from dotenv import load_dotenv
import os

st.title("Gabi Chat ̶a̶")

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    #######
    
    # Exibe a mensagem do usuário imediatamente
    with st.chat_message("user"):
        st.markdown(prompt)
        
        
    chat_response = response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": chat_response})
    
    # Display user message in chat message container
    with st.chat_message("assistant"):
        st.markdown(chat_response)