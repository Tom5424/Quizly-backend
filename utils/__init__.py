from .yt_downloader import get_video_info
from .gemini import set_prompt
from .choices import answer_choices


def get_transcribe_audio():
    from .whisper import transcribe_audio
    return transcribe_audio