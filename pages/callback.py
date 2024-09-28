import streamlit as st
from auth.auth_utils import handle_auth0_callback

st.title("Processing Authentication...")

# Handle the callback from Auth0
query_params = st.experimental_get_query_params()
if 'code' in query_params:
    code = query_params['code'][0]
    
    # Process the authorization code and get the token
    token = handle_auth0_callback(st.experimental_get_query_params())
    
    # Store the token in session state
    st.session_state['token'] = token
    
    # Clear query parameters and redirect to the main page
    st.experimental_set_query_params()
    st.success("You are now logged in! Redirecting to the homepage...")
    st.experimental_set_query_params(page='main')
else:
    st.error("No authorization code found. Please try logging in again.")