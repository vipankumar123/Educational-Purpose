from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_credentials():
    token_path = "token.json"
    credentials = Credentials.from_authorized_user_file(token_path, scopes=["https://www.googleapis.com/auth/youtube.force-ssl"])
    return credentials

def check_video_settings(youtube, video_id):
    video_response = youtube.videos().list(
        part='snippet',
        id=video_id
    ).execute()
    if video_response['items']:
        video_snippet = video_response['items'][0]['snippet']
        comments_enabled = video_snippet.get('comments', {}).get('allowComments', True)
        print(f"Video Title: {video_snippet['title']}")
        print(f"Comments Enabled: {comments_enabled}")
        return comments_enabled
    else:
        print(f"Video with ID {video_id} not found.")
        return False
    
def write_comment(youtube, video_id, comment_text):
    try:
        comment_response = youtube.commentThreads().insert(
            part='snippet',
            body={
                'snippet': {
                    'videoId': video_id,
                    'topLevelComment': {
                        'snippet': {
                            'textOriginal': comment_text
                        }
                    }
                }
            }
        ).execute()
        print(f"Comment added successfully: {comment_response['snippet']['topLevelComment']['snippet']['textOriginal']}")
        return True
    except Exception as e:
        print(f"Error adding comment: {e}")
        return False


def comment_on_url(credentials, url):
    youtube = build("youtube", 'v3', credentials=credentials)
    try:
        video_url = url
        video_id = video_url.split("v=")[1]
        print(f"video -id: {video_id}")
        video_setting = check_video_settings(youtube, video_id)
        if video_setting:
            comment_text = write_comment(youtube, video_id, "Keep it up!!")
            if not comment_text:
                print("not comment on video!!")
            else:
                print("successfully commnet on video.")
        else:
            print("comment not allowed on this video!!")
    except Exception as e:
        print("error------", e)


credentials = get_credentials()

url = "https://www.youtube.com/watch?v=lfiPjoKxznU"

comment_on_url(credentials, url)


