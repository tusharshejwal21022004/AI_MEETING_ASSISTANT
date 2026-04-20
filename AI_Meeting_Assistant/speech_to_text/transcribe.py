import os
import whisper

os.environ["PATH"] += os.pathsep + r"C:\Users\VIRAJ\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin"

model = whisper.load_model("small")

def convert_to_text():
    audio_path = r"C:\Users\VIRAJ\OneDrive\Desktop\AI_Meeting_Assistant\live_audio.wav"

    if not os.path.exists(audio_path):
        print("No audio file")
        return ""

    result = model.transcribe(audio_path, language="en")

    text = result["text"].strip()

    print("Text:", text)

    return text