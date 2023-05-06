import streamlit as st
from PIL import Image
import io
import requests
import cv2
from geopy.geocoders import Nominatim

def get_image_location(image):
    # Extract the GPS info from the image metadata
    exif_data = image._getexif()
    gps_info = exif_data.get(34853) if exif_data else None

    if gps_info:
        # Extract latitude and longitude from the GPS info
        latitude = gps_info[2][0] + gps_info[2][1] / 60 + gps_info[2][2] / 3600
        longitude = gps_info[4][0] + gps_info[4][1] / 60 + gps_info[4][2] / 3600

        # Reverse geocode the coordinates to get the location
        geolocator = Nominatim(user_agent="image-geolocation")
        location = geolocator.reverse(f"{latitude}, {longitude}")

        return location.address

    return None

def main():
    # Rest of your code...

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

    # Rest of your code...

if __name__ == '__main__':
    main()
