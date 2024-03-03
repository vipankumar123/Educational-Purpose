from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import os

credentials_path = "C:/Users/Hy_vipan/Downloads/secret.json"

def get_credentials():
    token_path = "token.json"
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
    credentials = flow.run_local_server(port=0)

    with open(token_path, "w") as token_file:
        token_file.write(credentials.to_json())

    return credentials

try:
    credentials = get_credentials()
except FileNotFoundError as e:
    print("error----", e)
