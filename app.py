from auth0_component import login_button
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

def show_homepage():
    st.title("Welcome to Huerta! You're logged in!")

clientId = os.getenv('clientId', 'default-client-id')
domain = os.getenv('domain', 'default-domain')


st.title('Welcome to Huerta! Please log in.')

if 'user_info' not in st.session_state:
    with st.echo():
        user_info = login_button(clientId = clientId, domain = domain)
        if user_info:
            st.write(f'Hi {user_info["nickname"]}')
            # st.write(user_info) # some private information here
else:
    show_homepage()

if 'user_info' not in st.session_state:
    st.write("Please login to continue")

    
