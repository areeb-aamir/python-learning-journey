from dotenv import load_dotenv
import os
from anthropic import Anthropic

load_dotenv()   # .env file ko "load" karta hai — ab uske andar ki values available hain

api_key = os.getenv("ANTHROPIC_API_KEY")   # .env se key nikalo, environment variable ki tarah

client = Anthropic(api_key=api_key)   # Anthropic se "connection" banaya

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=100,
    messages=[
        {"role": "user", "content": "Hello Claude, tum kaise ho?"}
    ]
)

print(response.content[0].text)
