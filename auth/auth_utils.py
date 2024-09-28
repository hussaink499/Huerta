from authlib.integrations.requests_client import OAuth2Session

AUTH0_DOMAIN = 'your-auth0-domain'
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
REDIRECT_URI = 'http://localhost:8501/callback'

def get_auth0_login_url():
    # Set up OAuth2 session for Auth0
    auth0 = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope="openid profile email", redirect_uri=REDIRECT_URI)
    authorization_url, state = auth0.authorization_url(f'https://{AUTH0_DOMAIN}/authorize')
    return authorization_url
