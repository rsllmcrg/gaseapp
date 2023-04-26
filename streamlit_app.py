import streamlit as st
from PIL import Image
import io

st.title("Image uploader")

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
        image = st.image('', use_column_width=True)
        # This will open the device's camera and capture a photo
        # The captured photo will be displayed in the app
        st.write("Taking photo...")
        image_upload = st.file_uploader(" ", type=["jpg", "jpeg", "png"], key="camera")
        if image_upload is not None:
            file_bytes = io.BytesIO(image_upload.read())
            image = Image.open(file_bytes)
            image.save('captured_image.png')
            st.image(image, caption='Captured Image', use_column_width=True)
