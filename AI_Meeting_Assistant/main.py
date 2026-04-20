from meeting_connector.meet_meeting import (
    open_meeting,
    raise_hand,
    lower_hand,
    unmute_mic,
    mute_mic,
    leave_meeting
)

from audio_capture.capture_audio import get_audio
from speech_to_text.transcribe import convert_to_text
from ai_response.generate_response import generate_reply
from text_to_speech.speak import speak_text
from speaker_detection.detect_speaker import detect_speaker
from summary_module.generate_summary import create_summary
from summary_module.extract_actions import extract_actions

import time

open_meeting()
time.sleep(5)

last_text = ""
skip_next = False
speaker_memory = {}

while True:
    print("\n--- Listening ---")

    if skip_next:
        skip_next = False
        print("Cooldown cycle skipped")
        time.sleep(1)
        continue

    time.sleep(1)

    ok = get_audio()

    if not ok:
        print("No audio file")
        continue

    text = convert_to_text()

    if not text:
        continue

    cleaned_text = text.lower().strip()

    if "stop meeting" in cleaned_text:
        leave_meeting()
        print("Meeting ending...")
        break

    if len(cleaned_text) > 3 and cleaned_text != last_text:

        wake_words = ["aiqod", "assistant", "bot"]

        if (("?" in text or
             "how" in cleaned_text or
             "what" in cleaned_text or
             "why" in cleaned_text or
             "can" in cleaned_text or
             "could" in cleaned_text or
             "do" in cleaned_text or
             "is" in cleaned_text)
             and (any(word in cleaned_text for word in wake_words) or "?" in text)):

            parts = text.split(" and ")

            for part in parts:
                clean_part = part.strip()

                if len(clean_part) > 2:

                    speaker = detect_speaker()
                    print("Speaker:", speaker)

                    previous = speaker_memory.get(speaker, "")
                    combined_text = previous + " " + clean_part

                    reply = generate_reply(combined_text)
                    print("AI Reply:", reply)

                    speaker_memory[speaker] = clean_part

                    if len(speaker_memory) > 5:
                        speaker_memory.clear()

                    short_reply = reply.split(".")[0]

                    if len(short_reply) < 5:
                        short_reply = reply[:120]

                    raise_hand()
                    time.sleep(1)

                    unmute_mic()
                    time.sleep(1.5)

                    speak_text(short_reply)

                    time.sleep(1)

                    mute_mic()
                    lower_hand()

                    skip_next = True

                    with open("meeting_log.txt", "a", encoding="utf-8") as f:
                        f.write("Speaker: " + speaker + "\n")
                        f.write("Text: " + clean_part + "\n")
                        f.write("AI: " + reply + "\n\n")

                    break

            last_text = cleaned_text

        else:
            print("No valid question for AI")

    else:
        print("Repeated or unclear speech")

with open("meeting_log.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

if not full_text.strip():
    full_text = "No meeting data available"

summary = create_summary(full_text)

print("\nFinal Summary:")
print(summary)

with open("final_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

actions = extract_actions(full_text)

print("\nAction Items:")
print(actions)

with open("final_actions.txt", "w", encoding="utf-8") as f:
    f.write(actions)