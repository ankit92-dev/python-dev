from transformers import pipeline

# Load DialoGPT model for conversational text generation
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

print("DialoGPT Chatbot (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    # Generate a response
    response = chatbot(user_input, max_length=100, num_return_sequences=1)
    print("Bot:", response[0]["generated_text"])