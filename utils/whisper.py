import whisper


def transcribe_audio():
    model = whisper.load_model("base")
    result = model.transcribe("audio.mp3")
    print(result["text"])