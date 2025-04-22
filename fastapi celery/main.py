from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        'C:/Users/Hy_vipan/Downloads/secret1.json',
        scopes=SCOPES
    )

    credentials = None
    try:
        credentials = flow.run_local_server(port=0)
    except FileNotFoundError:
        print("file not found!!")

    return credentials


def main():
    credentials = authenticate()
    if credentials:
        access_token = credentials.token
        authenticate_link = f'https://drive.google.com/?authuser=0&usp=drivesdk&auth_token={access_token}'
        print("google drive auth link", authenticate_link)
    else:
        print("link not found!!")

if __name__ == "__main__":
    main()