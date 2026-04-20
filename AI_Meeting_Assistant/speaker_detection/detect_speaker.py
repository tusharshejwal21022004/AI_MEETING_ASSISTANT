from pyannote.audio import Pipeline
import librosa
import torch
import os

pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    token="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"
)

def detect_speaker():
    audio_file = r"C:\Users\VIRAJ\OneDrive\Desktop\AI_Meeting_Assistant\live_audio.wav"

    if not os.path.exists(audio_file):
        return "No Speaker"

    waveform, sample_rate = librosa.load(audio_file, sr=None, mono=True)
    waveform = torch.tensor(waveform).unsqueeze(0)

    diarization = pipeline({
        "waveform": waveform,
        "sample_rate": sample_rate
    })

    speakers = []

    for segment, track, label in diarization.speaker_diarization.itertracks(yield_label=True):
        speakers.append(label)

    if speakers:
        return speakers[-1]

    return "Unknown Speaker"