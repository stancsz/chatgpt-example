# README
# Intro
This code uses the OpenAI API to generate a response to a user-provided prompt, while also logging the user's input and the API's response to a file. It uses the os module to get the API key from the environment variable OPENAI_API_KEY, the re module to clean the topic name to be used in the log file name and the openai module to interact with the OpenAI API. It uses a while loop to continuously prompt the user for input and generate responses from the API. If the user inputs 'exit', the loop breaks and the log file is closed. The script set max_tokens, temperature, top_p, frequency_penalty, presence_penalty as well.

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