from dotenv import load_dotenv
import os
from google import genai
from datetime import datetime
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def time() -> str :
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Current Time is {current_time}"

def add(a: int, b: int) -> int:
    """Add Two Numbers together."""
    return a + b


def sub(a: int, b: int) -> int:
    """Subtracts Two Numbers."""
    return a - b

content = input("You: ")
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=content,
    config={"tools": [add, sub, time]}
)
print(response)
print(response.text)

