import streamlit as st

# Configure the Streamlit app
st.set_page_config(
    page_title="My Streamlit App",
    layout="wide",
    initial_sidebar_state="expanded",
    showGithubCorner=False  # Set this to False to hide the GitHub icon
)

# Your Streamlit app code goes here
st.write("Hello, World!")
