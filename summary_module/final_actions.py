from extract_actions import extract_actions

with open(r"C:\Users\VIRAJ\OneDrive\Desktop\AI_Meeting_Assistant\meeting_log.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

actions = extract_actions(full_text)

print("\nAction Items:")
print(actions)