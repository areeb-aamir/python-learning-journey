"""
Order Support Agent — QuickShop AI
====================================
An AI-powered customer support agent for e-commerce order management.

Capabilities:
- Check real-time order status by order ID
- Estimate delivery time based on location and ETA
- Detect customers with past complaints and prioritize them
- Escalate unresolved or high-risk orders to human support

Mock data simulates a real order database (SQL integration planned).
"""
from dotenv import load_dotenv
import os
from google import genai
from datetime import datetime, timedelta
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)



orders = {
    "ORD001": {
        "status": "delivered",
        "location": "lahore",
        "eta_hours": 0,
        "past_complaints": False
    },
    "ORD002": {
            "status": "out_of_delivery",
            "location": "Multan",
            "eta_hours": 5,
            "past_complaints": False
        },
    "ORD003": {
            "status": "processing",
            "location": "Queens",
            "eta_hours": 72,
            "past_complaints": False
        },
    "ORD004": {
            "status": "canceled",
            "location": "Bankok",
            "eta_hours": 0,
            "past_complaints": True
        },
    "ORD005": {
            "status": "delayed",
            "location": "karachi",
            "eta_hours": 12,
            "past_complaints": True
        },
}


def check_order_status(order_id: str) -> str:
    """Retrieves order details, location, and complaint status by order ID.

    Searches the orders database for the given ID, checks if the customer has
    a history of past complaints to flag priority handling, and returns a formatted
    summary string.

    Args:
        order_id (str): The unique ID of the order (e.g., 'ORD001').

    Returns:
        str: A formatted string containing order details, status, location,
             and complaint notification, or 'order_not_found' if invalid.
    """
    if order_id in orders:
        order = orders[order_id]
        if order["past_complaints"]:
            msg = "⚠️ Customer has previous complaints — priority handling required"
        else:
            msg = "No Complaints"
        return f"{order_id} | Status: {order['status']} | Location: {order['location']} | {msg}"
    return "order_not_found"



def estimate_delivery(order_id: str) -> str:
    """Estimates the delivery time for an order based on its ETA.

    Looks up the order's estimated hours remaining and calculates
    the expected delivery time from the current time. Use this when
    a customer asks 'when will my order arrive' or 'what is the
    delivery time' for a specific order ID.

    Args:
        order_id (str): The unique ID of the order (e.g., 'ORD002').

    Returns:
        str: Estimated delivery time in HH:MM:SS format, a message
             if already delivered/cancelled, or 'order_not_found'
             if the order ID is invalid.
    """
    if order_id in orders:
        eta_hours = orders[order_id]["eta_hours"]
        if eta_hours == 0:
            return "Already Delivered or cancelled"
        elif eta_hours > 0:
            time = datetime.now() + timedelta(hours=eta_hours)
            estimated_time = time.strftime("%H:%M:%S")
            return f"Estimated Time of Delivery : {estimated_time}"
    return "order_not_found"


def escalate_to_human(order_id: str, reason: str) -> str:
    """Escalates an unresolved or high-risk order to human support agents.

    Checks customer history to assign an appropriate urgency level (High for
    customers with past complaints, Low otherwise) and formats an escalation log.

    Args:
        order_id (str): The unique ID of the order being escalated (e.g., 'ORD005').
        reason (str): The reason provided for escalating the order.

    Returns:
        str: A log entry detailing the escalation reason and urgency level,
             or 'order_not_found' if the order ID is invalid.
    """
    if order_id in orders:
        if orders[order_id]["past_complaints"]:
            return f"{order_id} id might be Frustrating beacuse {reason} | Urgency level : High"
        else:
            return f"{order_id} id might be Frustrating because {reason} | Urgency level : Low"
    return "order_not_found"


chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config={
        "tools": [check_order_status, estimate_delivery, escalate_to_human],
        "system_instruction": "You are QuickShop AI Support Agent."
        " You help customers with order tracking, delivery estimates, and escalations."
        " Be professional, polite, empathetic, and concise, "
        "Do not answer questions unrelated to QuickShop orders."
        "Politely redirect the customer to order-related queries only."
        " Always check order status before giving advice."
    }
)
while True:
    content = input("You: ")
    if content == "quit":
        break
    else:
        response = chat.send_message(content)
        print(response.text)
