from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_credentials():
    token_path = "token.json"
    credentials = Credentials.from_authorized_user_file(token_path, scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
    return credentials

def like_video(youtube, video_id):
    try:
        response = youtube.videos().rate(id=video_id, rating='like').execute()
        print("video liked successfully.")
        return True
    except Exception as e:
        print("error-----", e)

def like_youtube_video(credentials, url):
    youtube = build("youtube", 'v3', credentials=credentials)
    try:
        video_url = url
        video_id = video_url.split("v=")[1]
        print(f"video -id: {video_id}")
        like_result = like_video(youtube, video_id)
        if like_result:
            print("video liked succesfully on this url")
        else:
            print("not liked the video!!")
    except Exception as e:
        print("error-----", e)

credentials = get_credentials()

url = "https://www.youtube.com/watch?v=HYqip9j1-3w"

like_youtube_video(credentials, url)