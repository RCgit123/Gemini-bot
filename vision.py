from dotenv import load_dotenv
load_dotenv() # loading all the env varibles

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load Gemini pro model and get responses
model=genai.GenerativeModel("gemini-pro-vision")
def get_response(input,image):
    if input!="":
        response=model.generate_content([input,image])
    
    else:
        response=model.generate_content(image)
    return response.text


## Streamlit setup
st.set_page_config(page_title="Gemini Image-to-text")

st.header("Gemini App")
input=st.text_input("Input prompt: ",key="input")

upload_file=st.file_uploader("Choose an image..",type=["jpeg","jpg","png"])
image=''
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image,caption="Uploaded image",use_column_width=True)
    
submit=st.button("Tell me about it")

if submit:
    response=get_response(input,image)
    st.subheader("The Response is")
    st.write(response)


