import streamlit as st
import easyocr
import numpy as np
import cv2
from PIL import Image
from io import BytesIO

# Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'hi'])

# Function to convert uploaded image to OpenCV format
def load_image(image_file):
    img = Image.open(image_file)  # Open the uploaded image using PIL
    img_np = np.array(img)        # Convert PIL image to numpy array (OpenCV format)
    # Convert RGB to BGR (OpenCV default format)
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
    return img_cv

# Function to extract text from image
def extract_text_from_image(image):
    results = reader.readtext(image, detail=0)
    return " ".join(results)

# Function to search keyword in text and highlight it
def highlight_keyword(text, keyword):
    if keyword.lower() in text.lower():
        highlighted = text.replace(keyword, f"**{keyword}**")
        return highlighted
    return text

# Streamlit app
st.title("OCR and Document Search Web Application")

# File uploader for image input
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the uploaded image into a numpy array using OpenCV
    image_cv = load_image(uploaded_file)

    # Extract text from the image using EasyOCR
    extracted_text = extract_text_from_image(image_cv)
    st.write("### Extracted Text:")
    st.write(extracted_text)

    # Search functionality
    keyword = st.text_input("Enter keyword to search:")
    if keyword:
        result = highlight_keyword(extracted_text, keyword)
        st.write("### Search Result:")
        st.markdown(result)
