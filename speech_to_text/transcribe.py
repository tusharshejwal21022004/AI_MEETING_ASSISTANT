import os
import requests
import time

API_KEY = "0402f56b96cc4109af216a5c4d4a780e"

def convert_to_text():
    audio_path = r"C:\Users\VIRAJ\OneDrive\Desktop\AI_Meeting_Assistant\live_audio.wav"

    if not os.path.exists(audio_path):
        print("No audio file")
        return ""

    headers = {
        "authorization": API_KEY
    }

    # Step 1: Upload audio
    with open(audio_path, "rb") as f:
        upload_response = requests.post(
            "https://api.assemblyai.com/v2/upload",
            headers=headers,
            data=f
        )

    audio_url = upload_response.json()["upload_url"]
    print("Audio uploaded successfully")

    # Step 2: Request transcription
    data = {
        "audio_url": audio_url,
        "speaker_labels": True,
        "speech_models": ["universal-2"]
    }

    transcript_response = requests.post(
        "https://api.assemblyai.com/v2/transcript",
        json=data,
        headers=headers
    )

    transcript_id = transcript_response.json()["id"]

    # Step 3: Poll until complete
    while True:
        polling = requests.get(
            f"https://api.assemblyai.com/v2/transcript/{transcript_id}",
            headers=headers
        ).json()

        if polling["status"] == "completed":
            utterances = polling.get("utterances", [])

            full_text = ""

            for item in utterances:
                speaker = item["speaker"]
                text = item["text"]

                line = f"Speaker {speaker}: {text}"
                print(line)

                full_text += line + "\n"

            return full_text.strip()

        elif polling["status"] == "error":
            print("Error:", polling["error"])
            return ""

        else:
            print("Processing...")
            time.sleep(3)