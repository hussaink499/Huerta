import streamlit as st
import pandas as pd
from openai_integration.chatgpt_utils import chatgpt_response
from auth.auth_utils import get_auth0_login_url

# Load event dataset
events_df = pd.read_csv('data/events.csv')

def main():
    st.title("Huerta Event App")

    menu = ["Login", "Find Events", "Chat with ChatGPT"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Login":
        login_url = get_auth0_login_url()
        st.write(f"[Login here]({login_url})")
    elif choice == "Find Events":
        st.subheader("Browse Events")
        st.write(events_df)
    elif choice == "Chat with ChatGPT":
        user_input = st.text_input("Tell ChatGPT what you're looking for:")
        if user_input:
            response = chatgpt_response(user_input, events_df)
            st.write(response)

if __name__ == '__main__':
    main()
