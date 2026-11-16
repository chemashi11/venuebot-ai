from langchain_core.tools import tool
from sqlalchemy.orm import Session
from app.models.resource import Resource
from app.models.booking import Booking
from datetime import datetime

# --- MOCK TOOLS FOR NOW ---
# In a production app, we would pass the DB session into these tools.
# For now, we will use mock data so you can see the AI reasoning process.

@tool
def check_availability(resource_type: str, date: str, time: str) -> str:
    """Checks if a specific resource (table, hall, study_spot) is available for a given date and time."""
    # Mock logic: Let's pretend everything is available except the study spot on Friday.
    if resource_type == "study_spot" and date.lower() == "friday":
        return "Sorry, the study spots are fully booked on Friday."
    
    return f"Good news! The {resource_type} is available on {date} at {time}."

@tool
def create_booking(customer_email: str, resource_type: str, date: str, time: str, food_order: str = "None") -> str:
    """Creates a booking for a customer and optionally places a food order."""
    # Mock logic for creating a booking
    return f"Booking confirmed for {customer_email}! {resource_type} on {date} at {time}. Food order: {food_order}. A staff alarm has been set for the kitchen."

# The list of tools the AI can use
agent_tools = [check_availability, create_booking]