import streamlit as st
import pandas as pd
# from openai_integration.chatgpt_utils import chatgpt_response
# from auth.auth_utils import get_auth0_login_url
from groq_integration.groq_utils import chat
# Load event dataset
events_df = pd.read_csv('data/events.csv')

def main():
    st.title("Huerta Event App")

    menu = ["Login", "Find Events", "Chat with ChatGPT"]
    choice = st.sidebar.selectbox("Menu", menu)

    user_input = st.text_input("Ask about events (e.g., 'Show me concerts in Miami')")

    # this is primitive
    if user_input:
        chat_output = chat(user_input)
        st.write(chat_output)

    # if choice == "Login":
    #     login_url = get_auth0_login_url()
    #     st.write(f"[Login here]({login_url})")
    # elif choice == "Find Events":
    #     st.subheader("Browse Events")
    #     st.write(events_df)
    # elif choice == "Chat with ChatGPT":
    #     user_input = st.text_input("Tell ChatGPT what you're looking for:")
    #     if user_input:
    #         response = chatgpt_response(user_input, events_df)
    #         st.write(response)

def find_events(user_query):
    # get the event type
    # get the location
    # get the date

    return 0

if __name__ == '__main__':
    main()
