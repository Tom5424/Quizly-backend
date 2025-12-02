import whisper


def transcribe_audio(video_path):
    """Transcribe the video from the given video path."""


    model = whisper.load_model("tiny")
    result = model.transcribe(video_path, fp16=False, temperature=0, no_speech_threshold=0, condition_on_previous_text=True)
    return result["text"]