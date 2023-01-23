import os
import re
import openai

# Setting the API key to use the OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Setting up the logging feature by creating a file with the topic name
topic = "demo"
history_log = 'history/' + re.sub('[^0-9a-zA-Z]+', '', topic) + '.log'

# Initializing the prompt and context variables
prompt = ""
context = ""


# How many last prompt will the script pass to the next prompt

def estimate_tokens(text):
    """
    As per https://openai.com/api/pricing/, prices are per 1,000 tokens. You can think of tokens as pieces of words, where 1,000 tokens is about 750 words. This paragraph is 35 tokens.
    :param text:
    :return:
    """
    return len(text.split()) / 0.75


def reduce_context(context, limit=3000):
    context_list = context.split()
    new_size = int(limit / 0.75)
    return " ".join(context.split()[-new_size:])


while True:
    # Prints '>>' to indicate user input is needed
    print(">>")
    # User input for the prompt
    prompt = input()
    # If the user inputs 'exit', the loop breaks
    if prompt == 'exit':
        break

    # Sends the prompt and context to the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="context:" + context + "\n" + "prompt:" + prompt,
        temperature=0.7,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Writes the user's input to the log file
    file = open(history_log, "a")
    file.write(prompt)
    # Writes the API's response to the log file
    file.write(response["choices"][0]["text"] + "\n")
    # Prints the API's response
    print(response["choices"][0]["text"] + "\n")
    # Adds the prompt and response to the context variable
    context += prompt + "/n"
    print(f"context[{context}]")
    print(estimate_tokens(context))
    print(reduce_context(context))
    # Closes the log file
    file.close()
