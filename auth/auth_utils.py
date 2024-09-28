import os
from authlib.integrations.requests_client import OAuth2Session
from urllib.parse import urlencode


# Load sensitive information from environment variables
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN', 'dev-7u71b7e3a5xy6nfx.us.auth0.com')
CLIENT_ID = os.getenv('CLIENT_ID', 'vBzSObIq88lSobt8d6v1FsEiaBM0mxfZ')
CLIENT_SECRET = os.getenv('CLIENT_SECRET', 'ej3tZDjyhyD1Ykk8TBSPhwN9p8va_onpL6pbtnO59_3PNFNe15Z1PkckWIxwiV8X')
REDIRECT_URI = os.getenv('REDIRECT_URI', 'http://localhost:8501/pages/callback')
AUDIENCE = os.getenv('AUDIENCE', 'https://dev-7u71b7e3a5xy6nfx.us.auth0.com/api/v2/')

def get_auth0_login_url():
    # Set up OAuth2 session for Auth0
    auth0 = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope="openid profile email", redirect_uri=REDIRECT_URI)
    authorization_url, state = auth0.create_authorization_url(
        f'https://{AUTH0_DOMAIN}/authorize',
        audience=AUDIENCE
        )
    return authorization_url

def handle_auth0_callback(url):
    auth0 = OAuth2Session(CLIENT_ID, CLIENT_SECRET, redirect_uri=REDIRECT_URI)
    token = auth0.fetch_token(
        f'https://{AUTH0_DOMAIN}/oauth/token',
        authorization_response=url,
        client_secret=CLIENT_SECRET,
        audience = AUDIENCE
    )
    return token
def get_logout_url():
    params = {
        'client_id': CLIENT_ID,
        'returnTo': 'http://localhost:8501'
    }
    return f'https://{AUTH0_DOMAIN}/v2/logout?{urlencode(params)}'