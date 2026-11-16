from langchain_core.tools import tool
from sqlalchemy.orm import Session
from app.models.resource import Resource
from app.models.booking import Booking
from app.models.user import User  # <-- ADDED THIS IMPORT
from app.core.database import SessionLocal
from datetime import datetime
from app.services.alarm_service import create_food_order_with_alarm

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
        
        return f"Yes, we have {len(resources)} {resource_type}(s) available on {date} at {time}."
    finally:
        db.close()

@tool
def create_booking(customer_email: str, resource_type: str, date: str, time: str, food_order: str = "None") -> str:
    """Creates a booking for a customer and optionally places a food order."""
    db: Session = SessionLocal()
    try:
        # 1. Find the user by email
        user = db.query(User).filter(User.email == customer_email).first()
        
        # If the user doesn't exist, tell the AI to ask them to register
        if not user:
            return f"Customer with email {customer_email} not found. Please ask them to register first."

        # 2. Find the first available resource
        resource = db.query(Resource).filter(Resource.type == resource_type).first()
        if not resource:
            return f"Cannot book: No {resource_type} exists in the database."
            
        # 3. Create the booking using the REAL user ID
        new_booking = Booking(
            customer_id=user.id, # <-- Now we use the real ID!
            resource_id=resource.id,
            start_time=datetime.now(),
            end_time=datetime.now(),
            status="confirmed",
            total_price=resource.base_price_per_hour
        )
        db.add(new_booking)
        db.commit()
        
        return f"Booking confirmed for {customer_email}! Booking ID is {new_booking.id}. {resource.name} on {date} at {time}."
    finally:
        db.close()

@tool
def order_food_for_booking(customer_email: str, booking_id: int, menu_item_name: str, quantity: int, serve_time: str) -> str:
    """
    Orders food for an existing booking and sets a staff alarm.
    serve_time must be in ISO format, e.g., '2026-11-17T19:00:00'
    """
    db: Session = SessionLocal()
    try:
        # Parse the string time into a Python datetime object
        serve_datetime = datetime.fromisoformat(serve_time)
        
        # Call the alarm service we created earlier
        result = create_food_order_with_alarm(
            db=db,
            booking_id=booking_id,
            menu_item_name=menu_item_name,
            quantity=quantity,
            serve_time=serve_datetime
        )
        return result
    except Exception as e:
        return f"Failed to order food: {str(e)}"
    finally:
        db.close()

# The list of tools the AI can use (Defined AT THE BOTTOM)
agent_tools = [check_availability, create_booking, order_food_for_booking]