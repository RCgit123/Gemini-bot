from dotenv import load_dotenv
load_dotenv() # loading all the env varibles

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_response(question):
    response=model.generate_content(question)
    return response.text


## streamlit app setup

st.set_page_config(page_title="Q&A Demo")

# Add a background image using CSS
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('https://images.unsplash.com/photo-1593371256584-ac70d0ab43d1?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');  /* Replace with the actual path or URL */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;  /* Ensure text visibility on the background */
        }
        
        .st-b7, .st-bb {
            font-weight: bold !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.header("**Gemini LLM App**")

input=st.text_input("**Input:** ",key="input")
submit=st.button("Ask the question")

## When submit is clicked

if submit:
    response=get_response(input)
    st.subheader("The Response is")
    st.write(response)