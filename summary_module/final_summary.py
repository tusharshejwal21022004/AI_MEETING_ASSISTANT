from generate_summary import create_summary

with open(r"C:\Users\VIRAJ\OneDrive\Desktop\AI_Meeting_Assistant\meeting_log.txt", "r", encoding="utf-8") as f:
    full_text = f.read()

summary = create_summary(full_text)

print("\nFinal Summary:")
print(summary)