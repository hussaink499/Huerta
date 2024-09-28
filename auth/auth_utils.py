from auth0_component import login_button
import streamlit as st

clientId = "egQFK33bYZ0rlJY8AZkSu5kFGhE7jOij"
domain = "dev-7u71b7e3a5xy6nfx.us.auth0.com"

user_info = login_button(clientId, domain = domain)
st.write(user_info)