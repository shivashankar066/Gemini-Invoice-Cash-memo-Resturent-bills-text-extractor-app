import streamlit as st
import os
import pathlib
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load OpenAI model and get response
def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    return response.text


# Function to convert image into bytes
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# initialize the streamlit
st.set_page_config(page_title="Invoice text extractor, Gemini LLM App")
st.header("Gemini Image Application")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Click on image")

input_prompt = """
               You are an expert in understanding invoices or Bills or Cash Memo.
               You will receive input images as invoices or any Bills or Cash Memo&
               you will have to answer questions based on the input image
               """

# If ask button is clicked
if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("The Response is:")
    st.write(response)

st.info("author: Shivashankar")
