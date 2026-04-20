import requests

conversation_history = []

def generate_reply(text):
    global conversation_history

    conversation_history.append("User: " + text)

    url = "http://localhost:11434/api/generate"

    prompt = "Reply like a real human in an ongoing meeting. Never mention AI. Use previous conversation context if relevant. Keep answer short, professional, maximum 1 sentence:\n" + "\n".join(conversation_history[-4:]) + "\nAI:"
    
    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    reply = result["response"]

    conversation_history.append("AI: " + reply)

    conversation_history = conversation_history[-10:]

    return reply