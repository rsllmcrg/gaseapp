import streamlit as st
from PIL import Image

def main():
    st.set_page_config(page_title="Golden Apple Snail Eggs Detection", page_icon=":guardsman:", layout="wide")
    st.markdown("<h1 style='text-align: center;'>Golden Apple Snail Eggs Detection</h1>", unsafe_allow_html=True)

    # Check if the user is logged in
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        show_login_page()
    else:
        show_main_page()

def show_login_page():
    st.write("<h2 style='text-align: center;'>Login</h2>", unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        # Perform login verification (add your own logic here)
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.experimental_rerun()

def show_main_page():
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
            image
