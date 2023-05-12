import streamlit as st
from PIL import Image

# Function to extract and convert GPS coordinates to decimal degrees
def get_gps_coordinates(exif_data):
    gps_info = exif_data.get(34853)  # GPSInfo tag for GPS data
    
    if gps_info is None:
        return None
    
    # Extract GPS coordinates
    lat_values = gps_info[2]
    lon_values = gps_info[4]
    
    # Convert degrees/minutes/seconds to decimal degrees
    latitude = lat_values[0] + lat_values[1] / 60 + lat_values[2] / 3600
    longitude = lon_values[0] + lon_values[1] / 60 + lon_values[2] / 3600
    
    # Handle negative coordinates
    if gps_info[1] == 'S':
        latitude = -latitude
    if gps_info[3] == 'W':
        longitude = -longitude
    
    return latitude, longitude

# Streamlit web app
def main():
    st.title("GPS Coordinates Extractor")
    
    # Upload image file
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Photo", use_column_width=True)
        
        # Extract Exif metadata
        exif_data = image._getexif()
        
        # Check if Exif metadata exists and has GPS information
        if exif_data is not None and 34853 in exif_data:
            # Extract and convert GPS coordinates
            latitude, longitude = get_gps_coordinates(exif_data)
            
            if latitude is not None and longitude is not None:
                st.subheader("GPS Coordinates")
                
                if isinstance(latitude, float) and isinstance(longitude, float):
                    st.write(f"Latitude: {latitude:.6f}")
                    st.write(f"Longitude: {longitude:.6f}")
                else:
                    st.write(f"Latitude: {latitude}")
                    st.write(f"Longitude: {longitude}")
            else:
                st.write("No GPS coordinates found.")
        else:
            st.write("No GPS information found in Exif metadata.")

if __name__ == "__main__":
    main()
