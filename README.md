# README
The purpose of this project is to provide a way to use powerful GPT-3 language models, such as ChatGPT, in a low-code environment. This will enable developers to incorporate natural language processing capabilities into their applications with minimal effort. By using these powerful GPT-3 models, developers will be able to create more accurate and reliable natural language processing systems.

# Why
ChatGPT is a powerful GPT-3 language model that is designed to be used in chatbot applications. It is more powerful than other GPT-3 models because it uses a deep learning-based approach to generate natural language responses. This approach allows ChatGPT to generate more natural and accurate responses than other GPT-3 models.


# How it works
## Setup
Get your API key from, set it as your environment variable `OPENAI_API_KEY`, then run `main.py`
https://beta.openai.com/account/api-keys
## Terminating
just prompt `exit` to exit
```
>>
exit

Process finished with exit code 0
```
## Logs
After executing your api calls, find your logs under `history/{your topic name}.log`

This Python code is using the OpenAI API to generate responses to user input in a loop. The code starts by importing necessary modules and setting the API key. Then, it sets up logging by creating a file with the topic name. The code defines two functions, estimate_tokens and reduce_context, which are used to determine the number of tokens in a given text and to reduce the size of the context variable, respectively. The code then enters a while loop, in which it prompts the user for input, and uses the OpenAI API to generate a response to the input. The response, along with the user's input, is written to a log file, and the context variable is updated. The loop continues until the user enters "exit", at which point the code breaks out of the loop and the log file is closed.
context: 
- https://stancsz.medium.com/keeping-the-gpt-3-context-alive-875e1624adf4
- https://help.openai.com/en/articles/6787051-does-chatgpt-remember-what-happened-earlier-in-the-conversation

# Demo
```
givme me a list of 10 programming languages

1. Java
2. C/C++
3. Python
4. JavaScript
5. Ruby
6. PHP
7. Swift
8. Go
9. Rust
10. Kotlin
for each of the programming language above, write a short intro of each

1. Java: Java is a general-purpose, object-oriented programming language developed by Sun Microsystems in 1995. It is a powerful, secure language that can be used to create a wide variety of applications.

2. C/C++: C and C++ are two of the most popular programming languages in the world. C is a powerful, low-level language used for system and application programming, while C++ is an object-oriented language that is used for developing large software applications.

3. Python: Python is an interpreted, high-level, general-purpose programming language. It is a versatile language that can be used to create desktop applications, web applications, data science projects, and more.

4. JavaScript: JavaScript is a high-level, interpreted programming language commonly used to create interactive web applications. It is a popular language that is used by developers all over the world.

5. Ruby: Ruby is an object-oriented programming language designed to be easy to learn and use. It is a popular language used to create web applications and has powerful features such as metaprogramming.

6. PHP: PHP is a popular server-side scripting language used to create dynamic websites and web applications. It is a flexible language that can be used for a variety of tasks.

7. Swift: Swift is a powerful, open-source programming language developed by Apple in 2014. It is a modern language used to create applications for iOS and macOS.

8. Go: Go is a general-purpose programming language developed at Google in 2009. It is a statically typed language that is designed to be easy to read, write, and maintain.

9. Rust: Rust is a modern, low-level programming language developed at Mozilla in 2010. It is a safe, fast language that can be used to create a variety of applications.

10. Kotlin: Kotlin is a statically typed, cross-platform programming language developed at JetBrains in 2011. It is a modern language that is used to create Android and web applications.

```

# How to Contribution
We welcome contributions from the community to this project. If you would like to contribute, feel free to fork or clone the repository and submit pull requests with your changes. We also welcome suggestions and bug reports. Please make sure to follow the GitHub contribution guidelines when submitting changes.


# Future Plan
I'm working on some wrapper and a better way to structure the API calls in a NLP efficient prompt structure. After that I'd like to make cloud function native api framework for lambda or gcp cloud functions. After that will be working on building custom function and perhaps building an API re-seller startup. If you like to work on these things together, [let's chat!](https://www.linkedin.com/in/stan-chen/).   