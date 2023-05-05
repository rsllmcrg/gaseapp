import streamlit as st
from PIL import Image
import io
import requests
import cv2

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Perform authentication logic here
        if username == "your_username" and password == "your_password":
            st.success("Logged in successfully")
            st.experimental_set_query_params(logged_in=True)
        else:
            st.error("Invalid username or password")
    if "logged_in" not in st.experimental_get_query_params():
        login()
    else:
        main()
        
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

        option = st.radio("", ("Upload", "Camera"))

        if option == "Upload":
            st.write("Please drag and drop a photo below:")
            image_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
            if image_file is not None:
                img = Image.open(image_file)
                st.image(img, caption="Uploaded photo", use_column_width=True)

        elif option == "Camera":
            st.write("Please drag and drop a photo below:")
            image_file = st.camera_input("")
            if image_file is not None:
                img = Image.open(image_file)
                st.image(img, caption="Uploaded photo", use_column_width=True)

            uploaded_file = st.sidebar.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                st.image(image, caption='Uploaded image', use_column_width=True)


    elif choice == "About":
        st.write("""

        The Golden Apple Snail Eggs Detection Application is a computer vision-based application that aims to detect the presence of golden apple snail eggs in rice fields. The golden apple snail is a notorious pest in rice fields, and its eggs can cause significant damage to crops. This application provides a quick and efficient way to detect the presence of these eggs, allowing farmers to take appropriate measures to prevent further damage.

        The application is built using deep learning techniques and is trained on a large dataset of images of golden apple snail eggs. It uses convolutional neural networks (CNNs) to automatically extract features from the input images and classify them as either containing or not containing golden apple snail eggs. The application can be run on a desktop computer or a mobile device and can be accessed through a user-friendly interface.

        The Golden Apple Snail Eggs Detection Application has the potential to revolutionize the way farmers detect and prevent golden apple snail infestations. By providing a fast and accurate way to detect the presence of snail eggs, the application can help farmers save time and money and reduce the use of harmful pesticides.
        """)


if __name__ == '__main__':
    main()
