import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Define a function to display an image
def show_image(img):
    st.image(img, use_column_width=True)

# Define a function to capture an image from the user's webcam
def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    return frame

# Create a Streamlit web app
st.title("Image Uploader")

# Create a button for uploading an image using drag and drop
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Use the PIL library to read the image data
    image = Image.open(uploaded_file)

    # Display the uploaded image
    show_image(image)

# Create a button for taking a photo using the user's webcam
if st.button("Take a Photo"):
    # Capture an image from the user's webcam
    frame = capture_image()

    # Convert the image from OpenCV format to PIL format
    image = Image.fromarray(np.uint8(frame))

    # Display the captured image
    show_image(image)
