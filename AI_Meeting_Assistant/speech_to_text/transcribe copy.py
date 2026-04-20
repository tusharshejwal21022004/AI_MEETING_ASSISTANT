import os
import whisper

os.environ["PATH"] += os.pathsep + r"C:\Users\VIRAJ\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin"

def convert_to_text(audio_file):
    model = whisper.load_model("base")
    file_path = os.path.join("speech_to_text", audio_file)
    result = model.transcribe(file_path)
    return result["text"]