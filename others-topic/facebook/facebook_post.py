# pip install facebook-sdk
import requests
import facebook as fb

page_id = "257292494128308"
access_token = "EAAEwkBzvJbIBO0HpJfCyNdhig6CWjDt7QPfKoz96J69VSxbj4Ci9irIw66FW4gWQzG8xlfIJP08H3SUZCffjqG6b3waEodEGZBahZAqBFszrdVoczG3nXhp8fiTFbHXzQN6BNapPNHQImoYKKTaoik9XEgjGR97mEUeArjXtuIST5ldYTfzXfAmTKDVsFntZCcXO40a8QRmp4COpCWBZARmfwjQZBoXX1WQzvh99ISTsFCuydPub3SdhuAZBAF17ncvJvUtKgZDZD"
graph = fb.GraphAPI(access_token=access_token, version='3.0')
page_info = graph.get_object(f'/{page_id}?fields=access_token')

page_access_token = page_info.get("access_token")

post_url = f"https://graph.facebook.com/{page_id}/feed"

response = requests.post(post_url, params={"message": "hlo guys, This is python programing channel #python", 'access_token': page_access_token})

if response.status_code == 200:
    print("post successfully created.")
else:
    print("respose", response.text)
    print("error---------------")
