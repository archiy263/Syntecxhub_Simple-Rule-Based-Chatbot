# Simple Rule-Based Conversational Chatbot

## 📌 Project Description
This project implements a **conversational chatbot using pattern matching**, inspired by **AIML-style rule-based Artificial Intelligence**.  
The chatbot identifies user intents based on predefined patterns and responds using **rule-based logic** without using any machine learning algorithms.

This project is developed as part of the **Syntecxhub Artificial Intelligence Internship**.

---

## 🎯 Task Requirements Covered
As per the internship task instructions, this project fulfills the following:

- Create a conversational bot using **pattern matching (rule-based / AIML-style)**
- Support **intents** such as greeting, help, and small talk
- Generate **rule-based responses**
- Add a **small knowledge base** to answer domain-related questions
- Make the chatbot **interactive via console**
- **Log conversation history** for future reference

---

## 🧠 AI Approach Used
This chatbot follows a **Symbolic AI (Rule-Based AI)** approach.  
Instead of learning from data, the chatbot uses predefined rules and patterns to simulate intelligent conversation.

### Logic Flow:

User Input
↓
Text Normalization
↓
Pattern Matching (Intent Detection)
↓
Knowledge Base Lookup
↓
Rule-Based Response Generation
↓
Conversation Logging


This approach is conceptually similar to **AIML (Artificial Intelligence Markup Language)** systems.

---

## ⚙️ Features
- Pattern matching using regular expressions
- Intent recognition (greeting, help, thanks, goodbye, small talk)
- Knowledge base for answering domain questions
- Console-based interactive chatbot
- Automatic conversation logging with timestamps
- Lightweight and easy to extend

---

## 🛠️ Technologies Used
- Python 3
- Regular Expressions (`re`)
- JSON (for intents and knowledge base)
- File handling for logging conversations

No machine learning or external libraries are used.

---

## 📂 Project Structure

Project_3 Simple Rule-Based Chatbot/
│
├── chatbot.py # Main chatbot logic
├── intents.json # Intent patterns and knowledge base
├── chat_log.txt # Conversation history log
├── requirements.txt # Dependencies (minimal)
└── README.md


---

## ▶️ How to Run the Chatbot

### Step 1: Open the Project Folder
'''bash
cd Project_3 Simple Rule-Based Chatbot

Step 2: Run the Chatbot
python chatbot.py


💬 Sample Interaction

🤖 Rule-Based AI Chatbot (type 'exit' to quit)

You: hello
Bot: Hello! How can I help you?

You: what is ai
Bot: Artificial Intelligence is the simulation of human intelligence in machines.

You: thanks
Bot: You're welcome!

You: exit
Bot: Goodbye! Have a great day.


📝 Notes

This chatbot does not use machine learning

Intelligence is achieved using pattern matching and rule-based reasoning

The knowledge base can be easily expanded by editing intents.json

All conversations are automatically saved in chat_log.txt
