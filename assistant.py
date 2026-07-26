
import os
import cohere
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("COHERE_API_KEY")

# Initialize Cohere ClientV2
co = cohere.ClientV2(api_key=api_key)

def ask_ai(question):
    try:
        response = co.chat(
            # Updated to active model name:
            model="command-r-plus-08-2024",
            messages=[{"role": "user", "content": question}]
        )
        return response.message.content[0].text
    except Exception as e:
        print(f"Cohere API Error: {e}")
        return "I am having trouble connecting to my AI service right now."