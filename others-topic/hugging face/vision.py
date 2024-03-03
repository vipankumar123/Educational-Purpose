from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image
import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones
def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app
st.set_page_config(page_title="Uncover-Picture-Story")

st.header("Uncover the Story about Your Pictures🕵️‍♂️💡")
input=st.text_input("Input Prompt: ",key="input", placeholder="Optional")

# Subheader for user help
st.text("Example Input Text: Writing a blog on the picture...")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit=st.button("Tell me about the image")

## If ask button is clicked
if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)