import streamlit as st

# Inject custom CSS to hide the hamburger menu
hide_menu_style = """
<style>
div.stButton button:first-child {
    display: none;
}
</style>
"""

# Render the CSS
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Your Streamlit app code goes here
st.title("My Streamlit App")
st.write("Hello, World!")
