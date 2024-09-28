# Huerta

Key files and Directories Guide

/data
    Contains sample dataset, events.csv. 
    Events.csv structure 

    event_id, event_name, event_date, location, description, category, price 

/auth
    Contains authentification logic for auth0. auth_utils.py should handle the logic for logging in and verifying users with auth0.

/openai_integration
    Handles logic for integrating openai api. I want a chatbot feature where gpt has access to the sample dataset. 

app.py
    Main entry point for streamlit app. User interface, handle user inout, and call helper functions like auth0 and chatgpt.

requirements.txt 
    Lists all the dependencies needed to run the app, like streamlit, pandas, openai, authlib, etc. When cloning or deploying (like with defang), all dependencies can be installed with pip install -r requirements.txt. 

