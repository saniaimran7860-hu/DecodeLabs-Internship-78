
# -----------------------------------------
# Beginner-Level Rule-Based AI Chatbot
# -----------------------------------------

# Step 1: Print a welcome message
print("===================================")
print(" Welcome to My AI Chatbot!")
print(" Type 'exit', 'quit', or 'bye' to stop.")
print("===================================")

# Step 2: Create a dictionary of predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! Nice to meet you.",
    "how are you": "I am fine, thank you! How are you?",
    "name": "My name is Python Chatbot.",
    "help": "Sure! You can ask me about my name, time, date, or a joke.",
    "time": "I cannot check the real-time clock yet.",
    "date": "I cannot check today's date yet.",
    "joke": "Why did the computer go to the doctor? Because it had a virus!",
    "thank you": "You're welcome! Happy to help.",
    "bye": "Goodbye! Have a wonderful day!",
    "what can you do": "I can answer simple predefined questions.",
    "who created you": "I was created using Python programming."
    "what are you doing": "I am chatting with you!",
    "why": "Can you please explain your question?",
    "what do you understand": "I understand simple predefined questions."}

# Step 3: Run the chatbot continuously
while True:

    # Ask the user to enter a message
    user_input = input("You: ")

    # Step 4: Sanitize the input
    # Convert text to lowercase and remove extra spaces
    clean_input = user_input.lower().strip()

    # Step 5: Check if the user wants to exit
    if clean_input in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! Have a nice day!")
        break

    # Step 6: Get the response from the dictionary
    # If the input is not found, show the default message
    reply = responses.get(clean_input, "I do not understand.")

    # Step 7: Display the chatbot's response
    print("Chatbot: " + reply)

# -----------------------------------------
# End of Chatbot Program
# -----------------------------------------