import os
import re
import openai

# Setting the API key to use the OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")

# Setting up the logging feature by creating a file with the topic name
topic = "demo"
history_log = 'history/' + re.sub('[^0-9a-zA-Z]+', '', topic) + '.log'
file = open(history_log, "a")

# Initializing the prompt and context variables
prompt = ""
context = ""

while True:
    # Prints '>>' to indicate user input is needed
    print(">>")
    # User input for the prompt
    prompt = input()
    # If the user inputs 'exit', the loop breaks
    if prompt == 'exit':
        break
    # Writes the user's input to the log file
    file.write(prompt)
    # Sends the prompt and context to the OpenAI API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="context:" + context + "\n\n" + "prompt:" + prompt,
        temperature=0.7,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Writes the API's response to the log file
    file.write(response["choices"][0]["text"] + "\n")
    # Prints the API's response
    print(response["choices"][0]["text"] + "\n")
    # Adds the prompt and response to the context variable
    context += "\n".join([context, prompt, response["choices"][0]["text"]])

# Closes the log file
file.close()
