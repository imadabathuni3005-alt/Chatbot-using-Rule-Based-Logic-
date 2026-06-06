from datetime import datetime
print("=" * 40)
print("      RULE-BASED CHATBOT")
print("=" * 40)
print("Type 'bye' to exit the chatbot.\n")
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there!",
    "hey": "Hey! Welcome!",
    "how are you": "I'm fine. Thanks for asking!",
    "what is your name": "I am a Rule-Based Chatbot.",
    "who created you": "I was created using Python.",
    "python": "Python is a popular programming language.",
    "thank you": "You're welcome!",
    "bye": "Goodbye! Have a nice day!"
}
while True:
    user_input = input("You: ").lower().strip()

    if user_input == "bye":
        print("Bot:", responses["bye"])
        break

    elif user_input in responses:
        print("Bot:", responses[user_input])

    elif "time" in user_input:
        print("Bot: Current Time =", datetime.now().strftime("%H:%M:%S"))

    elif "date" in user_input:
        print("Bot: Today's Date =", datetime.now().strftime("%d-%m-%Y"))

    elif "help" in user_input:
        print("Bot: You can ask about greetings, date, time, or my name.")

    else:
        print("Bot: Sorry, I don't understand that.")

print("\nChatbot Closed.")