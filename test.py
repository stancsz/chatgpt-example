from unittest import TestCase

from ChatGPT import ChatApp


class Test(TestCase):
    def test_chatgpt_interactive(self):
        print("<< (chatgpt_py, enter your prompts)")
        app = ChatApp(model="gpt-3.5-turbo") # if you have access, you can use `model="gpt-4"`
        while True:
            res = app.chat(input())
            print(res)
    def test_load_convo(self):
        from ChatGPT import ChatApp
        app = ChatApp(model="gpt-3.5-turbo",
                      load_file='models/chat_model_you-are-a-translator-you-tran-1680306043-381102.json')  # if you have access, you can use `model="gpt-4"`
        while True:
            res = app.chat(input())
            print(res)

    def test_chatgpt3_5(self):
        app = ChatApp(model="gpt-3.5-turbo") # if you have access, you can use `model="gpt-4"`
        message_list = ["how are you?",
                   "I want to know how to learn python quickly?",
                   "What are the best resources for this?",
                   "what should I learn first?"
                   ]
        for m in message_list:
            res = app.chat(m)
            print(m, res)