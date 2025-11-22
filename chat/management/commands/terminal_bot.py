from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class Command(BaseCommand):   # <-- Class name must be Command
    help = "Start a terminal chat with a ChatterBot instance."

    def handle(self, *args, **options):
        bot = ChatBot("TerminalBot")
        trainer = ListTrainer(bot)
        
        # Define list of possible conversation and train them 
        trainer.train([
            "Good morning!",
            "Good morning. How are you?",
            "I am doing very well, thank you for asking.",
            "You're welcome.",
            "Who created you?",
            "I am chatbot by MSCS-633 student as assignment project",
            "I am releated to Advance Artificial Course",
            "what do you like?",
            "I like to play FIFA"
        ])

        print("TerminalBot is ready! Type 'quit' to exit.\n")

        while True:
            text = input("user: ")
            if text.strip().lower() in {"quit", "exit"}:
                print("bot: Goodbye!")
                break
            response = bot.get_response(text)
            print(f"bot: {response}")
