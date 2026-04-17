from rag_module.store_memory import store_text
from ai_response.generate_response import generate_reply

store_text("Ajinkya sir said deploy on Azure")

reply = generate_reply("What did sir decide?")

print(reply)