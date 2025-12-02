from utils.yt_downloader import get_video_audio_path
from utils.whisper import transcribe_audio
from utils.gemini import set_prompt


def create_quiz(video_url):
   """Generates a quiz prompt from a video by extracting, transcribing, and processing its audio."""


   audio_path = get_video_audio_path(video_url)
   if audio_path is not None: 
      transcript_text = transcribe_audio(audio_path)
      prompt = set_prompt(transcript_text)
      return prompt