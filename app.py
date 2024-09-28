import streamlit as st
from auth.auth_utils import get_auth0_login_url, handle_auth0_callback, get_logout_url

def show_homepage():
    st.title("Welcome to Huerta!")
    st.write("You are logged in!")

st.title("Login with Auth0")

# Handle the callback
query_params = st.experimental_get_query_params()
if 'code' in query_params:
    code = query_params['code'][0]
    url = st.experimental_get_query_params()
    token = handle_auth0_callback(url)
    st.session_state['token'] = token
    # Clear query parameters and reload the page using JavaScript
    st.experimental_set_query_params()
    st.write("Redirecting...")
    st.markdown('<meta http-equiv="refresh" content="0; url=/" />', unsafe_allow_html=True)

# Check if the user is already logged in
if 'token' not in st.session_state:
    # Display the login link
    login_url = get_auth0_login_url()
    st.write(f"[Login]({login_url})")
else:
    # Display the homepage content
    show_homepage()
    # Display the logout link
    logout_url = get_logout_url()
    st.write(f"[Logout]({logout_url})")

