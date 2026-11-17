from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.models.booking import Order
from app.models.menu import MenuItem

def create_food_order_with_alarm(
    db: Session, 
    booking_id: int, 
    menu_item_name: str, 
    quantity: int, 
    serve_time: datetime
) -> str:
    """
    Creates an order and calculates the alarm time based on prep time.
    """
    # 1. Find the menu item
    menu_item = db.query(MenuItem).filter(MenuItem.name.ilike(f"%{menu_item_name}%")).first()
    if not menu_item:
        return f"Error: We don't have {menu_item_name} on the menu."

    # 2. Calculate when the staff alarm should ring
    # Alarm Time = Serve Time - Prep Time
    alarm_time = serve_time - timedelta(minutes=menu_item.prep_time_minutes)

    # 3. Save the order to the database
    new_order = Order(
        booking_id=booking_id,
        menu_item_id=menu_item.id,
        quantity=quantity,
        requested_serve_time=serve_time,
        alarm_time=alarm_time,
        status="pending"
    )
    db.add(new_order)
    db.commit()

    return f"Order placed for {quantity}x {menu_item.name}. Staff alarm set for {alarm_time.strftime('%H:%M')}."