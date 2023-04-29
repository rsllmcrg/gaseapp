import streamlit as st
from PIL import Image
import io

# Create login page
username = st.sidebar.text_input('Username')
password = st.sidebar.text_input('Password', type='password')

if st.sidebar.button('Login'):
    # Check if username and password match database
    # Redirect to main app page if login is successful
    st.success('Logged in as {}'.format(username))

if st.sidebar.button('Register'):
    # Add new user to database
    st.success('You have successfully registered!')

# Function to detect eggs in image
def detect_eggs(image):
    # Your egg detection algorithm goes here
    # Return the annotated image with egg detections
    return annotated_image

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

        option = st.selectbox("", ("Drag and drop a photo", "Take a photo"))

        if option == "Drag and drop a photo":
            st.write("Please drag and drop a photo below:")
            image_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
            if image_file is not None:
                img = Image.open(image_file)
                st.image(img, caption="Uploaded photo", use_column_width=True)

                # Detect eggs in the uploaded image
                annotated_image = detect_eggs(img)

                # Display the annotated image
                st.image(annotated_image, caption="Annotated photo", use_column_width=True)

        elif option == "Take a photo":
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

                    # Detect eggs in the captured image
                    annotated_image = detect_eggs(image)

                    # Display the annotated image
                    st.image(annotated_image, caption="Annotated photo", use_column_width=True)

    elif choice == "About":
        st.write("""

        The Golden Apple Snail Eggs Detection Application is a computer vision-based application that aims to detect the presence of golden apple snail eggs in rice fields. The golden apple snail is a notorious pest in rice fields, and its eggs can cause significant damage to crops. This application provides a"
