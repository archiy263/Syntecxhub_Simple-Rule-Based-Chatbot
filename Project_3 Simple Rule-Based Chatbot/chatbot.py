import re
import json
from datetime import datetime

# Load knowledge base
with open("intents.json", "r") as file:
    intents = json.load(file)

# Intent patterns (pattern matching)
patterns = {
    "greeting": re.compile(r"\b(hi|hello|hey)\b"),
    "goodbye": re.compile(r"\b(bye|goodbye|exit)\b"),
    "thanks": re.compile(r"\b(thanks|thank you)\b")
}

responses = {
    "greeting": "Hello! How can I help you?",
    "goodbye": "Goodbye! Have a great day.",
    "thanks": "You're welcome!"
}

def log_chat(user, bot):
    with open("chat_log.txt", "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] User: {user}\n")
        f.write(f"[{time}] Bot: {bot}\n")

def get_response(user_input):
    user_input = user_input.lower()

    for intent, pattern in patterns.items():
        if pattern.search(user_input):
            return responses[intent]

    for intent in intents["intents"]:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input:
                return intent["responses"][0]

    return "Sorry, I didn’t understand that."

print("🤖 Rule-Based AI Chatbot (type 'exit' to quit)")

while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    bot = get_response(user)
    print("Bot:", bot)
    log_chat(user, bot)
