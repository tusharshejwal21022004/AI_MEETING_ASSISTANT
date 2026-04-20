import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

def get_audio():
    fs = 16000
    duration = 5

    print("Recording started...")

    try:
        audio = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype='float32',
            device=1
        )

        sd.wait()

        volume = abs(audio).mean()
        print("Volume:", volume)

        if volume < 0.0005:
            print("Silence detected")
            return False

        audio = audio * 3
        audio = np.clip(audio, -1, 1)

        write(
            r"C:\Users\VIRAJ\OneDrive\Desktop\AI_Meeting_Assistant\live_audio.wav",
            fs,
            audio
        )

        print("Recording saved")
        return True

    except Exception as e:
        print("Audio error:", e)
        return False


if __name__ == "__main__":
    get_audio()