import os

def generate_response(user_input):
    """
    This function simulates an LLM response.
    Replace this logic with OpenAI or Bedrock API later.
    """
    return f"I understand you said: {user_input}. I'm learning to respond intelligently."

def chatbot():
    print("GenAI Chatbot (type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        
        response = generate_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()
