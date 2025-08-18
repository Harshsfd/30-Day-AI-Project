# Next-Level CHATBOT with clear chat feature

import re
import random
from datetime import datetime
import os  # For clearing the screen

# Dictionary mapping keywords to a list of possible responses
responses = {
    "hello": ["Hi there! How can I help you?", "Hello! Nice to see you!", "Hey! How's it going?"],
    "hi": ["Hello!", "Hi! How are you?", "Hey there!"],
    "hey": ["Hey! Nice to meet you!", "Hi there!", "Hello!"],
    "how are you": ["I'm just a chatbot, but I'm doing great! How about you?", 
                    "Doing well! How about you?", 
                    "I'm fine, thanks for asking!"],
    "help": ["Sure! What do you need help with?", "I'm here to assist you. Ask me anything!"],
    "bye": ["Goodbye! Have a great day!", "See you later!", "Bye! Take care!"],
    "goodbye": ["Goodbye! Stay safe!", "See you later!", "Take care!"],
    "thanks": ["You're welcome!", "No problem!", "Happy to help!"],
    "thank you": ["Anytime!", "No worries!", "Glad I could help!"],
    "what is your name": ["I'm Chatbot, your virtual assistant.", "You can call me Chatbot."],
    "your name": ["Chatbot at your service!", "I am Chatbot."],
    "joke": ["Why did the computer show up at work late? It had a hard drive!",
             "Why do programmers prefer dark mode? Because light attracts bugs!",
             "Why did the developer go broke? Because he used up all his cache!"],
    "date": [f"Today's date is {datetime.now().strftime('%d %B %Y')}"],
    "time": [f"The current time is {datetime.now().strftime('%H:%M:%S')}"],
    "history": ["By Harsh Bhardwaj","18 Aug 2025","Simple Chatbot"],
    "weather": ["I can't check real-time weather yet, but I hope it's nice where you are!"],
    "math": ["I can help with simple math: try typing 'add 5 10' or 'multiply 4 3'"],
    "default": ["I'm not sure how to respond to that. Can you ask something else?",
                "Hmm, I didn't understand that. Try asking differently.",
                "Sorry, I don't have a response for that yet."]
}

# Function to process simple math expressions
def handle_math(user_input):
    try:
        if "add" in user_input:
            numbers = [int(n) for n in re.findall(r'\d+', user_input)]
            return f"The sum is {sum(numbers)}"
        elif "subtract" in user_input:
            numbers = [int(n) for n in re.findall(r'\d+', user_input)]
            return f"The result is {numbers[0] - numbers[1]}"
        elif "multiply" in user_input:
            numbers = [int(n) for n in re.findall(r'\d+', user_input)]
            return f"The product is {numbers[0] * numbers[1]}"
        elif "divide" in user_input:
            numbers = [int(n) for n in re.findall(r'\d+', user_input)]
            return f"The result is {numbers[0] / numbers[1]}"
    except:
        return "I couldn't calculate that. Make sure you typed it correctly."

# Function to find response
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Check for math first
    if any(word in user_input for word in ["add", "subtract", "multiply", "divide"]):
        return handle_math(user_input)

    # Check all keywords and pick a random response if multiple options
    for keyword in responses:
        if re.search(keyword, user_input):
            return random.choice(responses[keyword])
    
    # Default response
    return random.choice(responses["default"])

# Main chatbot function
def chatbot():
    while True:
        # Print welcome message
        print("Welcome to the next-level chatbot! Type 'exit' to end the conversation or 'clear' to clear the chat.\n")
        
        while True:
            user_input = input("You: ")
            
            if user_input.lower() == 'exit':
                print("Chatbot: Goodbye! Have a wonderful day!")
                return  # Exit the program
                
            if user_input.lower() == 'clear':
                os.system('clear')  # For Linux / macOS. Use 'cls' for Windows.
                break  # Break inner loop to restart with welcome message
            
            response = chatbot_response(user_input)
            print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
