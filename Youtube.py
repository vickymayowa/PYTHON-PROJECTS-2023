# Downloading Youtube Videos Using python
import yt_dlp

# Enter the url for the download

url = input("Enter the Video Url Here:")
print(url)

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

    print("SuccessFully Downloaded your Youtube Video")
    # https://youtu.be/b1kbLwvqugk