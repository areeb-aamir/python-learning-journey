import streamlit as st
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


st.title("QuickShop Support 🛒")
st.write("Welcome to QuickShop Customer Support!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["parts"][0]["text"])

user_input = st.chat_input("Type your message...")


if user_input:
    st.session_state.messages.append({'role': 'user',
                                      "parts": [{"text": user_input}]})
    with st.chat_message("user"):
        st.write(user_input)
    config=types.GenerateContentConfig(
                    system_instruction=system_prompt)
    response = client.models.generate_content_stream(
    model="gemini-3.5-flash-lite",
    contents=st.session_state.messages,
    config=config
    )

    with st.chat_message("assistant"):
        full_response = ""
        for chunk in response:
            full_response += chunk.text
        st.write(full_response)
    st.session_state.messages.append({"role": "model",
                                       "parts": [{"text": full_response}]})
