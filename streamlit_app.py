import streamlit as st
from PIL import Image
import io

def main():
    st.set_page_config(page_title="Golden Apple Snail Eggs Detection", page_icon=":guardsman:", layout="wide")
    st.markdown("<h1 style='text-align: center;'>Golden Apple Snail Eggs Detection</h1>", unsafe_allow_html=True)

    # Create a menu with multiple pages
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Home":
        st.write("<p style='text-align: center; font-style: italic;'>The Golden Apple Snail Eggs Detection Application is a web application designed to detect the presence of Golden Apple Snail eggs in images. "
                 "The app uses image processing and machine learning techniques to identify and highlight the location of Golden Apple Snail eggs in the uploaded images.</p>", unsafe_allow_html=True)
        st.write("Please upload an image containing the rice field:")

    option = st.sidebar.selectbox(
        'Select an option:',
        ('Drag and Drop', 'Take a Photo'))

    if option == 'Drag and Drop':
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption='Uploaded Image', use_column_width=True)

    if option == 'Take a Photo':
        st.write("Click the button below to take a photo using your device's camera.")
        if st.button('Take a photo'):
            image_placeholder = st.empty()
            # This will open the device's camera and capture a photo
            # The captured photo will be displayed in the app
            st.write("Taking photo...")
            image_upload = st.file_uploader(" ", type=["jpg", "jpeg", "png"], key="camera")
            if image_upload is not None:
                file_bytes = io.BytesIO(image_upload.read())
                image = Image.open(file_bytes)
                image.save('captured_image.png')
                image_placeholder.image(image, caption='Captured Image', use_column_width=True)
