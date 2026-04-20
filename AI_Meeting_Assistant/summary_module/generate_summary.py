import requests

def create_summary(text):
    url = "http://localhost:11434/api/generate"

    prompt = f"Summarize this meeting text clearly:\n{text}"

    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    return result["response"]