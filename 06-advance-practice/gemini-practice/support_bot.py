from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

store_name = "QuickShop"


system_prompt = f"""
You are a friendly customer support agent of {store_name}.
You Help Customer in:
- Order tracking
- Returns aur refunds
- Product information
Always Be polite and Helpful.
If You don't Know somthing Say Clearly and respectfully.
"""

conversation_history = []


print(f"Welcome to {store_name} Support! (Type 'quit' to exit)")
print("-" * 40)



while True:
    prompt = input("You: ")
    if prompt.lower() == "quit":
        break
    else:
        conversation_history.append({'role': 'user',
                                      "parts": [{"text": prompt}]})
        config=types.GenerateContentConfig(
                system_instruction=system_prompt
                )
        response = client.models.generate_content_stream(
        model="gemini-3.5-flash-lite",
        contents=conversation_history,
        config=config
        )
        full_response = ""
        for chunk in response:
            full_response += chunk.text
            print(chunk.text, end="", flush=True)
            print()
        conversation_history.append({"role" : "model",
                                      "parts" :[{"text" : full_response}]})
