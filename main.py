from ChatGPT import ChatApp
app = ChatApp(model="gpt-3.5-turbo")
def main():
    while True:
        res = app.chat(input())
        print(res)

if __name__ == "__main__":
    main()