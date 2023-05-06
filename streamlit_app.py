import streamlit as st
from PIL import Image
import io
import requests
import cv2
from geopy.geocoders import Nominatim
from geopy import Point

def get_image_location(image):
    # Extract the GPS info from the image metadata
    exif_data = image._getexif()
    gps_info = exif_data.get(34853) if exif_data else None

    if gps_info:
        # Extract latitude and longitude from the GPS info
        latitude = gps_info[2][0] + gps_info[2][1] / 60 + gps_info[2][2] / 3600
        longitude = gps_info[4][0] + gps_info[4][1] / 60 + gps_info[4][2] / 3600

        # Create a Point object
        coordinates = Point(latitude, longitude)

        # Reverse geocode the coordinates to get the location
        geolocator = Nominatim(user_agent="image-geolocation")
        location = geolocator.reverse(coordinates)

        return location.address

    return None

def main():
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

                # Get the location of the uploaded image
                location = get_image_location(img)
                if location:
                    st.write("Image location:", location)
                else:
                    st.write("Location information not found in the image metadata.")

    elif choice == "About":
        st.write("""
        The Golden Apple Snail Eggs Detection Application is a computer vision-based application that aims to detect the presence of golden apple snail eggs in rice fields. The golden apple snail is a notorious pest in rice fields, and its eggs can cause significant damage to crops. This application provides a quick and efficient way to detect the presence of these eggs, allowing farmers to take appropriate measures to prevent further damage.

        The application is built using deep learning techniques and is trained on a large dataset of images of golden apple snail eggs. It uses convolutional neural networks (CNNs) to automatically extract features from the input images and classify them as either containing or not containing golden apple snail eggs. The application can be run on a desktop computer or a mobile device and can be accessed through a user-friendly interface.

        The Golden Apple Snail Eggs Detection Application has the potential to revolutionize the way farmers detect and prevent""")

        
if __name__ == '__main__':
    main()
