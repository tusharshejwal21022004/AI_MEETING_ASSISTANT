def detect_context(text):
    if "what" in text.lower() or "how" in text.lower():
        return "Question detected"
    return "Statement detected"