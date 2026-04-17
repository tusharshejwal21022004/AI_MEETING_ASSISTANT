import requests

def extract_actions(text):
    url = "http://localhost:11434/api/generate"

    prompt = f"Extract action items from this meeting conversation:\n{text}"

    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    return result["response"]