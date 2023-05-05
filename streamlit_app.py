import streamlit as st

def login():
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Perform authentication logic here
        if username == "Jean" and password == "abc1243":
            st.success("Logged in successfully")

            # Redirect to the main page
            st.experimental_set_query_params(logged_in=True)
        else:
            st.error("Invalid username or password")

def main():
    st.title("Login Page")

    # Check if the user is logged in
    if "logged_in" not in st.experimental_get_query_params():
        login()
    else:
        st.write("Welcome to the main page!")  # Replace this with your main page content

if __name__ == "__main__":
    main()
