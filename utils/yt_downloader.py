import yt_dlp


ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "media/downloads/%(title)s.%(ext)s",
    "quiet": True,
    "noplaylist": True,
}


def get_video_audio_path(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(url, download=False)
        duration = video_info.get("duration", 0)
        if duration <= 300:
            video_path = ydl.prepare_filename(video_info)
            return video_path