# README
The purpose of this Repo is to use `gpt-3.5-turbo` and `gpt-4` model from OpenAI, and saves the conversational models and easily manage them. This generates useful json output that can be used to deploy to other services.
# Usage
chats
```python
from ChatGPT import ChatApp
app = ChatApp(model="gpt-3.5-turbo")  # if you have access, you can use `model="gpt-4"`
while True:
    res = app.chat(input())
    print(res)
```
To exit, prompt `exit`, then you can find the conversation history model files in models folder
# Test Log
```
{
  "content": "Greetings, visitors from beyond the stars! I am your humble translator, here to assist you in understanding our language. Our language is unique, with melodious and flowing sounds that will surely captivate your senses. Let me guide you through our linguistic nuances and reveal the hidden depths of our communication. Together, we shall bridge the gap between our worlds and foster a deeper understanding of our diverse cultures. Welcome to our humble abode, dear visitors. Let us begin our journey of discovery and exploration!",
  "role": "assistant"
}
{
  "content": "Az\u018fizlarimiz, bu oldukca cilyax\u015fiy\u0259rin xuliqani!",
  "role": "assistant"
}

Process finished with exit code 1

```
after entering `exit` the conversational model file will be created:
```
models/chat_model_you-are-a-translator-you-tran-1680306043-381102.json
```

to reload your chat models, simply:
```python
from ChatGPT import ChatApp
app = ChatApp(model="gpt-3.5-turbo", load_file='models/chat_model_you-are-a-translator-you-tran-1680306043-381102.json')  # if you have access, you can use `model="gpt-4"`
while True:
    res = app.chat(input())
    print(res)
```

reloaded convo log
```
what's my last message
{
  "content": "Your last message was: \"translate: this is pretty cool stuffs\"",
  "role": "assistant"
}
translate: weeeee, we're flying
{
  "content": "Ziziziz, biz u\u00e7uruq!",
  "role": "assistant"
}
```