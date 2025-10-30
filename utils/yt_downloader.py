import json
import yt_dlp


URL = 'https://www.youtube.com/watch?v=BaW_jenozKc'
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "media/downloads/%(title)s.%(ext)s",
    "quiet": True,
    "noplaylist": True,
}


def get_video_info(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(URL, download=False)
        print(json.dumps(ydl.sanitize_info(info)))