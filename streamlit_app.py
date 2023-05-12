import streamlit as st
from PIL import Image

# Function to extract Exif metadata from an image
def get_exif_data(image):
    exif_data = image._getexif()  # Get the raw Exif data
    if exif_data is None:
        return None
    exif = {}  # Dictionary to store the parsed Exif data
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        exif[tag_name] = value
    return exif

# Streamlit web app
def main():
    st.title("Exif Metadata Extractor")
    
    # Upload image file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Extract and display Exif metadata
        exif = get_exif_data(image)
        if exif is not None:
            st.subheader("Exif Metadata")
            for key, value in exif.items():
                st.write(f"{key}: {value}")
        else:
            st.write("No Exif metadata found.")
            
if __name__ == "__main__":
    main()
