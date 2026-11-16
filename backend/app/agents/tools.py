from langchain_core.tools import tool
from sqlalchemy.orm import Session
from app.models.resource import Resource
from app.models.booking import Booking
from app.core.database import SessionLocal
from datetime import datetime

# Note: We create a fresh database session inside the tools 
# because the AI agent runs in a background thread.

@tool
def check_availability(resource_type: str, date: str, time: str) -> str:
    """Checks if a specific resource (table, hall, study_spot) is available for a given date and time."""
    db: Session = SessionLocal()
    try:
        # Query the real database for resources of this type
        resources = db.query(Resource).filter(Resource.type == resource_type).all()
        
        if not resources:
            return f"Sorry, we currently have no {resource_type} registered in our system."
        
        # For simplicity in this phase, we will assume it's available if it exists.
        # In the next phase, we will check the 'bookings' table for time conflicts.
        return f"Yes, we have {len(resources)} {resource_type}(s) available on {date} at {time}."
    finally:
        db.close()

@tool
def create_booking(customer_email: str, resource_type: str, date: str, time: str, food_order: str = "None") -> str:
    """Creates a booking for a customer and optionally places a food order."""
    db: Session = SessionLocal()
    try:
        # Find the first available resource of this type
        resource = db.query(Resource).filter(Resource.type == resource_type).first()
        
        if not resource:
            return f"Cannot book: No {resource_type} exists in the database."
            
        # NOTE: In a real app, we would parse the date/time string into a datetime object.
        # For now, we will just create the record so you can see it in the DB.
        new_booking = Booking(
            customer_id=1, # Hardcoded for now (we will use real Auth later)
            resource_id=resource.id,
            start_time=datetime.now(), # Placeholder
            end_time=datetime.now(),   # Placeholder
            status="confirmed",
            total_price=resource.base_price_per_hour
        )
        db.add(new_booking)
        db.commit()
        
        return f"Booking confirmed for {customer_email}! {resource.name} on {date} at {time}. Food order: {food_order}."
    finally:
        db.close()

# The list of tools the AI can use
agent_tools = [check_availability, create_booking]