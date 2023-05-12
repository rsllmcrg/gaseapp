#GASE Egg Hotspot Mapping Prototype App
#-------Dependencies-----------
import streamlit as st
from streamlit.web.cli import main 
import pandas as pd
import leafmap.foliumap as leafmap
#dependencies for gps
from PIL import Image
from PIL.ExifTags import TAGS
import piexif
#------START----
page_title = "GASEApp"
page_icon = ":seedling:"
layout = "centered"

st.set_page_config(page_title=page_title,page_icon=page_icon,layout=layout)
st.title(page_title + " " + page_icon)

st.markdown("<h1 style='text-align: center;'>Gase App</h1>", unsafe_allow_html=True)

#Read Google Sheets
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

#--------------------
def main():
    # Create a menu with multiple pages
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Select a page", menu)

    if choice == "Home":
        st.markdown("<h1 style='text-align: center;'>GAS Egg Detector</h1>", unsafe_allow_html=True)
        st.write("<p style='text-align: center; font-style: italic;'>Use these options to upload or capture Kuhol Eggs!</p>", unsafe_allow_html=True)
        st.write("Please upload an image containing GAS eggs:")

        option = st.radio("", ("Upload", "Camera"))
  
        if option == "Upload":
            st.write("Please drag and drop a photo below:")
            uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])
            if uploaded_file is not None:
                # Read the uploaded file and convert it into an image object
                img = Image.open(uploaded_file)
                st.image(img, caption="Uploaded photo", use_column_width=True)

                # Check if the image has Exif data
                if 'exif' in img.info:
                    # Get the Exif data
                    exif_dict = piexif.load(img.info['exif'])
                    
                    # Extract the GPS coordinates
                    gps_latitude = exif_dict["GPS"][piexif.GPSIFD.GPSLatitude]
                    gps_latitude_ref = exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef]
                    gps_longitude = exif_dict["GPS"][piexif.GPSIFD.GPSLongitude]
                    gps_longitude_ref = exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef]
                    
                    # Convert the GPS coordinates to degrees
                    lat = (gps_latitude[0][0] / gps_latitude[0][1] +
                           gps_latitude[1][0] / (60 * gps_latitude[1][1]) +
                           gps_latitude[2][0] / (3600 * gps_latitude[2][1]))
                    
                    if gps_latitude_ref == "S":
                        lat = -lat
                    
                    lon = (gps_longitude[0][0] / gps_longitude[0][1] +
                           gps_longitude[1][0] / (60 * gps_longitude[1][1]) +
                           gps_longitude[2][0] / (3600 * gps_longitude[2][1]))
                    
                    if gps_longitude_ref == "W":
                        lon = -lon
                    
                    st.write(f"Latitude: {lat}, Longitude: {lon}")
                    
#------------If the GPS are written, append to csv---------------------------
                    import pandas as df
                    df_master = pd.read_csv(st.secrets["public_gsheets_url"])
                    st.write(df_master)
                    # for csv_file in csv_list:
                    #     df_master = pd.read_csv(csv_file)
                    #     df_master.to_csv('gase_plots', mode='a', header=False, index=False)
                else:
                    st.write("This image does not have Exif data.")
            
        elif option == "Camera":
            st.write("Please drag and drop a photo below:")
            image_file = st.camera_input("")
            if image_file is not None:
                img = Image.open(image_file)
                st.image(img, caption="Uploaded photo", use_column_width=True)

                # Check if the image has Exif data
                if 'exif' in img.info:
                    # Get the Exif data
                    exif_dict = piexif.load(img.info['exif'])

                # Extract the EXIF data
            exif_dict = piexif.load(image.info['exif'])

            # Extract the GPS coordinates and convert to decimal degrees
            gps_latitude = exif_dict['GPS'][piexif.GPSIFD.GPSLatitude]
            gps_latitude_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLatitudeRef]
            gps_longitude = exif_dict['GPS'][piexif.GPSIFD.GPSLongitude]
            gps_longitude_ref = exif_dict['GPS'][piexif.GPSIFD.GPSLongitudeRef]
            gps_altitude = exif_dict['GPS'][piexif.GPSIFD.GPSAltitude]
            gps_altitude_ref = exif_dict['GPS'][piexif.GPSIFD.GPSAltitudeRef]

            lat = (gps_latitude[0][0]/gps_latitude[0][1] +
                   gps_latitude[1][0]/(60*gps_latitude[1][1]) +
                   gps_latitude[2][0]/(3600*gps_latitude[2][1]))
            if gps_latitude_ref == 'S':
                lat = -lat

            lon = (gps_longitude[0][0]/gps_longitude[0][1] +
                   gps_longitude[1][0]/(60*gps_longitude[1][1]) +
                   gps_longitude[2][0]/(3600*gps_longitude[2][1]))
            if gps_longitude_ref == 'W':
                lon = -lon

            alt = (gps_altitude[0]/gps_altitude[1])
            if gps_altitude_ref == 1:
                alt = -alt

            # Extract the UTC time and date
            utc_time = exif_dict['0th'][piexif.ImageIFD.DateTime].decode('utf-8')
            utc_time = datetime.strptime(utc_time, '%Y:%m:%d %H:%M:%S')

            # Display the GPS data and UTC time and date
            st.write(f"Latitude: {lat:.6f}, Longitude: {lon:.6f}, Altitude: {alt:.2f}")
            st.write(f"UTC Time: {utc_time}")


    elif choice == "About":
        st.markdown("<h1 style='text-align: center;'> About </p>", unsafe_allow_html=True)
        st.write("""
        The Golden Apple Snail Eggs Detection Application is a web application designed to detect the presence of Golden Apple Snail eggs in images.
        The app uses image processing and machine learning techniques to identify and highlight the location of Golden Apple Snail eggs in the uploaded images.

        The Golden Apple Snail Eggs Detection Application is a computer vision-based application that aims to detect the presence of golden apple snail eggs in rice fields. The golden apple snail is a notorious pest in rice fields, and its eggs can cause significant damage to crops. This application provides a quick and efficient way to detect the presence of these eggs, allowing farmers to take appropriate measures to prevent further damage.

        The application is built using deep learning techniques and is trained on a large dataset of images of golden apple snail eggs. It uses convolutional neural networks (CNNs) to automatically extract features from the input images and classify them as either containing or not containing golden apple snail eggs. The application can be run on a desktop computer or a mobile device and can be accessed through a user-friendly interface.

        The Golden Apple Snail Eggs Detection Application has the potential to revolutionize the way farmers detect and prevent golden apple snail infestations. By providing a fast and accurate way to detect the presence of snail eggs, the application can help farmers save time and money and reduce the use of harmful pesticides.
        """)
        st.write(""" Created by Marian De Chavez, Jean Recon, and Roselle Macaraig """)


#-+++++++++++++++++++++++++++++++++++++++
#------------------------------------------
#load main dataset
df = load_data(st.secrets["public_gsheets_url"])
#drop the Number customized column
df = df.drop('No', axis=1)

#Open Leafmap with Google Map Layer
# with st.echo():   
import streamlit as st
import leafmap.foliumap as leafmap
    
m = leafmap.Map(height="1020px", width="720px",center=[12.3, 122], zoom=6.5)
colors = ['blue','red']
vmin = 1
vmax = 100
m.add_colorbar(colors=colors, vmin=vmin, vmax=vmax, font_size=12)

#added layer
m.add_tile_layer(
    url="https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}",
    name="Google Satellite",
    attribution="Google",
    )
m.add_title("Golden Apple Snail Egg Heat Map", font_size="20px", align="center")


#Add the heatmap
# with st.echo():

gase_dataset = load_data(st.secrets["public_gsheets_url"])
m.add_heatmap(
    gase_dataset,
    latitude="Latitude",
    longitude='Longitude',
    value="Altitude",
    # name="Heat map",
    radius=12,
)

#This is used to display the map within the bounded settings of Width and Height
m.to_streamlit(width=700, height=500, add_layer_control=True)

#display DataFrame
df = load_data(st.secrets["public_gsheets_url"])
df

#-----------------------------------------
if __name__ == '__main__':
    main()
