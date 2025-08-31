# Task : 3 Basic Chatbot
# A simple rule-based chatbot program

def chatbot_response(user_input):
    user_input = user_input.lower()

# Convert to lower case for easy matching

    if user_input == "hello":
        return "Hii!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."
    
 # Main program

print("Chatbot is running ...Type 'bye' to exit.\n")

while True:
        user_message = input("You: ")
        reply = chatbot_response(user_message)
        print("Chatbot:", reply)

        if user_message.lower() == "bye":
            break
