import requests
import time

# Tumhari AssemblyAI API Key
API_KEY = "0402f56b96cc4109af216a5c4d4a780e"

# Audio file ka naam (same folder me hona chahiye)
filename = "live_audio.wav"

# Headers
headers = {
    "authorization": API_KEY
}

# Step 1: Audio upload
with open(filename, "rb") as f:
    upload_response = requests.post(
        "https://api.assemblyai.com/v2/upload",
        headers=headers,
        data=f
    )

audio_url = upload_response.json()["upload_url"]
print("Audio uploaded successfully")

# Step 2: Transcript request
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

print(transcript_response.json())

transcript_id = transcript_response.json()["id"]

# Step 3: Result check
while True:
    polling = requests.get(
        f"https://api.assemblyai.com/v2/transcript/{transcript_id}",
        headers=headers
    ).json()

    if polling["status"] == "completed":
        print("\nTranscript Result:")
        print(polling["text"])
        break

    elif polling["status"] == "error":
        print("Error:", polling["error"])
        break

    else:
        print("Processing...")
        time.sleep(3)