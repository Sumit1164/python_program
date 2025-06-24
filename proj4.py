import random
def chatbot():
    responses = {
        "hello": ["Hi there!", "Hello!", "Hey!"],
        "how are you": ["I'm good, thank you!", "Doing great, how about you?", "I'm fine, thanks for asking!"],
        "what's your name": ["I'm KEYA.", "I am a chatbot.", "You can call me KEYA mam."],
        "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"]
    }
    def get_response(user_input):
        for key in responses:
            if key in user_input:
                return random.choice(responses[key])
        return "Sorry, I don't understand that."
    print("Welcome to the CHO Chatbot!")
    print("My name is KEYA. Type 'bye' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
if __name__ == "__main__":
    chatbot()
print("I'LL COPY THE ENTIRE MESSAGE")
print("LET'S TALK! ENTER 'quit' TO EXIT...")
while True:
    user = input("YOU: " )
    print(f"BOT: {user}")
    if user == 'quit':
        break