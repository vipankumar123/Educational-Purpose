from pytube import YouTube
import requests
import os


def download_video(video_url, output_directory, desiered_resolution='480p'):
    try:
        yt = YouTube(video_url)

        video_stream = yt.streams.filter(res={desiered_resolution}).first()

        print(f"Downloading: {yt.title} in {desiered_resolution}")

        video_stream.download(output_directory)

        print("Download video completed..........")

        download_thumbnail(yt.thumbnail_url, output_directory=".")

    except Exception as e:
        print("error------", e)

def download_thumbnail(url, output_directory='.', video_title="thumbnail"):
    try:
        thumbnail_content = requests.get(video_url).content

        # save the thumbnail into output directory
        thumbnail_path = os.path.join(output_directory, f"{video_title}_thumbnail.jpg")
        with open(thumbnail_path, "wb") as thumbnail_file:
            thumbnail_file.write(thumbnail_content)

        print(f"Thumbnail downloaded: {thumbnail_path}")
    except Exception as e:
        print("error------", e)




if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=t2v_5Z_tEuQ"
    output_directory = "C:/Users/Hy_vipan/Documents/Training/pytube/output"
    desiered_resolution = '480p'

    download_video(video_url, output_directory, desiered_resolution)