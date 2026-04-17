import requests
from rag_module.retrieve_memory import retrieve_context

conversation_history = []

def generate_reply(text):
    global conversation_history

    context = retrieve_context(text)

    conversation_history.append("User: " + text)

    prompt = (
        "Reply like a real human in an ongoing meeting. "
        "Never mention AI. "
        "Use previous conversation context if relevant. "
        "Keep answer short, professional, maximum 1 sentence.\n\n"
        f"Relevant previous context: {context}\n\n"
        + "\n".join(conversation_history[-4:])
        + "\nAI:"
    )

    url = "http://localhost:11434/api/generate"

    data = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)

    result = response.json()

    reply = result["response"].strip()

    conversation_history.append("AI: " + reply)

    conversation_history = conversation_history[-10:]

    return reply