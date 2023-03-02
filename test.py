from unittest import TestCase

from ChatApp import ChatApp


class Test(TestCase):
    def test_chatgpt3(self):
        app = ChatApp()
        message_list = ["how are you?",
                   "I want to know how to learn python quickly?",
                   "What are the best resources for this?",
                   "what should I learn first?"
                   ]
        for m in message_list:
            res = app.chat(m)
            print(m, res)

