import streamlit as st
import piexif

def add_exif_data(image_data):
    # Create an empty EXIF dictionary
    exif_dict = {"0th": {}, "Exif": {}}

    # Add desired EXIF data to the dictionary
    # Example: Adding a custom image description
    exif_dict["0th"][piexif.ImageIFD.ImageDescription] = "My Custom Description"

    # Convert the EXIF dictionary to bytes
    exif_bytes = piexif.dump(exif_dict)

    # Insert the EXIF data into the image
    image_data = piexif.insert(exif_bytes, image_data)

    return image_data

def main():
    # Capture image using Streamlit
    image_file = st.camera_input("")

    # Add EXIF data to the captured image
    image_data = add_exif_data(image_data)

    # Display the image with EXIF data
    st.image(image_data, use_column_width=True)

if __name__ == "__main__":
    main()
