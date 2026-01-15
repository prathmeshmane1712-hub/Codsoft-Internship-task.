print("Simple Chatbot")
print("Type 'bye' to exit")

while True:
    user_input = input("You: ").lower()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user_input:
        print("Bot: I am fine. Thanks for asking!")

    elif "your name" in user_input:
        print("Bot: I am a simple chatbot.")

    elif "help" in user_input:
        print("Bot: I can answer basic questions like greetings and info.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I did not understand that.")
