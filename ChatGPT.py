import json
import os
import openai
import time
import re


class ChatApp:
    """A class to interact with OpenAI's GPT models for chat applications."""

    def __init__(self, model="gpt-4.0-turbo", load_file=''):
        """
        Initializes the ChatApp with a specific model and optionally loads a chat history.

        :param model: The model to be used for chat completions, default is "gpt-4.0-turbo".
        :param load_file: Path to a file to load previous chat history, default is an empty string.
        """
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = model
        self.messages = []
        if load_file:
            self.load(load_file)

    def chat(self, message):
        """
        Handles a chat message, saves or exits if special commands are used.

        :param message: The message from the user.
        :return: The response from the model.
        """
        if message == "exit":
            self.save()
            os._exit(1)
        elif message == "save":
            self.save()
            return "(saved)"
        self.messages.append({"role": "user", "content": message})
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self.messages
        )
        self.messages.append({"role": "assistant", "content": response["choices"][0]["message"]["content"]})
        return response["choices"][0]["message"]["content"]

    def save(self):
        """Saves the chat history to a JSON file."""
        try:
            ts = time.time()
            json_object = json.dumps(self.messages, indent=4)
            filename_prefix = self.messages[0]['content'][0:30]
            filename_prefix = re.sub('[^0-9a-zA-Z]+', '-', f"{filename_prefix}_{ts}")
            with open(f"models/chat_model_{filename_prefix}.json", "w") as outfile:
                outfile.write(json_object)
        except:
            os._exit(1)

    def load(self, load_file):
        """Loads chat history from a file.

        :param load_file: Path to the file containing the chat history.
        """
        with open(load_file) as f:
            data = json.load(f)
            self.messages = data

    def clear_chat(self):
        """Clears the chat history."""
        self.messages = []
        print("Chat history cleared.")

    def export_chat_to_txt(self, filename):
        """Exports the chat history to a text file.

        :param filename: The name of the text file to export to.
        """
        with open(filename, 'w') as file:
            for message in self.messages:
                role = message['role']
                content = message['content']
                file.write(f"{role}: {content}\n")
        print(f"Chat history exported to {filename}.")

    def get_chat_history(self):
        """Returns the chat history as a formatted string.

        :return: A string representing the chat history.
        """
        history = ""
        for message in self.messages:
            role = message['role']
            content = message['content']
            history += f"{role}: {content}\n"
        return history

    def set_model(self, model):
        """Sets the model used for chat completions.

        :param model: The model to be used.
        """
        self.model = model
        print(f"Model set to {model}.")
