from groq import Groq
from google.colab import userdata

client = Groq(
    api_key=API)

def chat_with_bot_3P1_70B(user_message):
    completion = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )

    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""

    return response

def chat_3P1_70B():
    print("Welcome to the AI Chatbot (Llama 3.1 70B). Type your message and press enter.")
    print("Type 'exit' to quit the chat.\n")

    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            print("Goodbye!")
            break

        bot_response = chat_with_bot_3P1_70B(user_message)
        print(f"Bot: {bot_response}\n")
