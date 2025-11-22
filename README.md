
# QA Chatbot (Django + ChatterBot)

This project is a simple **terminal-based conversational agent** built with **Django** and **ChatterBot** for MSCS-633 – Advanced Artificial Intelligence, Assignment 3.

Student: Suresh Ghimire
---

## Features

- Terminal client to chat with a bot (`python manage.py terminal_bot`)
- ChatterBot–powered conversation engine
- Basic training data demonstrating a short dialogue
- Simple, easy-to-understand Django project structure

---

## Technology Stack

- Python 3.12 (or compatible 3.x)
- Django
- ChatterBot
- spaCy (for natural language processing model used by ChatterBot)

---

## Project Structure

```text
qa_chatbot/
├─ chat/
│  ├─ management/
│  │  ├─ __init__.py
│  │  └─ commands/
│  │     ├─ __init__.py
│  │     └─ terminal_bot.py   # main terminal chat command
│  ├─ migrations/
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ qa_chatbot/
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ settings.py             # Django settings (INSTALLED_APPS includes "chat")
│  ├─ urls.py
│  └─ wsgi.py
├─ manage.py
└─ requirements.txt            # manifest of Python dependencies
```

---

## Prerequisites

- Python 3.12 (or another 3.x version supported by Django/ChatterBot)
- pip
- (Optional but recommended) virtual environment (venv)

---

## Installation

1. **Clone or download the repository**

   ```bash
   git clone <your-repo-url> qa_chatbot
   cd qa_chatbot
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   venv\Scripts\activate   # on Windows
   # source venv/bin/activate  # on macOS / Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Install the spaCy English model (required by ChatterBot)**

   ```bash
   python -m spacy download en_core_web_sm
   ```

---

## Running the Terminal Chatbot

From the project root (where `manage.py` lives), run:

```bash
python manage.py terminal_bot
```

If everything is installed correctly, you should see something similar to:

```text
TerminalBot is ready! Type 'quit' or 'exit' to stop.

user: Good morning!
bot: Good morning. How are you?
user: I am doing very well, thank you for asking.
bot: You're welcome.
user: Do you like hats?
bot: Yes, I like hats very much.
user: quit
bot: Goodbye!
```

---

## How It Works

- The custom management command **`terminal_bot`** (in `chat/management/commands/terminal_bot.py`) creates a `ChatBot` instance from ChatterBot.
- The bot is trained with a small list of example sentences using `ListTrainer`.
- A loop reads user input from the terminal and uses `bot.get_response()` to generate a reply.
- Typing `quit` or `exit` cleanly ends the chat session.

---

## Limitations

- The training data is intentionally small and simple for demonstration purposes. ChatterBot supports much larger corpora for more realistic conversations.

---

