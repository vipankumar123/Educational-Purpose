
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_credentials():
    token_path = "token.json"
    credentials = Credentials.from_authorized_user_file(token_path, scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
    return credentials

def subscriber_channal_link(youtube, video_id):
    channel_id = youtube.videos().list(part='snippet',id=video_id).execute()['items'][0]['snippet']['channelId']
    youtube.subscriptions().insert(part='snippet', body={'snippet': {'resourceId': {'channelId': channel_id}}}).execute()
    print("subscribed to channel successfully")
    return True

#https://www.youtube.com/watch?v=lfiPjoKxznU
def subscriber_channel(credentials, url):
    youtube = build("youtube", 'v3', credentials=credentials)
    try:
        video_url = url
        video_id = video_url.split("v=")[1]
        print(f"video -id: {video_id}")
        subscribe_result = subscriber_channal_link(youtube, video_id)
        if not subscribe_result:
            print("Not subscriberd the channel!!")
        else:
            print("successfully subscribed the channel.")
    except Exception as e:
        print("error-------", e)

credentials = get_credentials()

url = "https://www.youtube.com/watch?v=lfiPjoKxznU"

subscriber_channel(credentials, url)




