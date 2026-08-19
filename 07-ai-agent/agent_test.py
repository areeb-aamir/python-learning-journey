from dotenv import load_dotenv
import os
from google import genai
from datetime import datetime, timedelta
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

def adjust_time(hours: int, minutes: int, seconds: int, operation: str) -> str:
    """
    Adjusts the current time by adding or subtracting a given duration.

    Use this when the user wants to know what time it will be after adding
    or subtracting hours, minutes, or seconds from the current time.

    Args:
        hours: Number of hours to add or subtract (use 0 if not mentioned)
        minutes: Number of minutes to add or subtract (use 0 if not mentioned)
        seconds: Number of seconds to add or subtract (use 0 if not mentioned)
        operation: Either 'add' to add time, or 'subtract' to subtract time

    Returns:
        The resulting time as a string in HH:MM:SS format
    """
    now = datetime.now()
    adjustment = timedelta(hours=hours, minutes=minutes, seconds=seconds)
    if operation in ["add", "addition"]:
        result = now + adjustment
        return result.strftime("%H:%M:%S")

    elif operation in ["subtract", "sub"]:
        result = now - adjustment
        return result.strftime("%H:%M:%S")
    else:
        return "Invalid operation"



content = input("You: ")
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=content,
    config={"tools": [add, sub, time, adjust_time]}
)
print(response)
print(response.text)

