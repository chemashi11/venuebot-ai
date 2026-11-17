from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.core.database import get_db
from app.models.booking import Order
from pydantic import BaseModel

router = APIRouter()

class AlarmResponse(BaseModel):
    order_id: int
    item_name: str
    quantity: int
    serve_time: datetime
    status: str

@router.get("/alarms", response_model=list[AlarmResponse])
def get_active_alarms(db: Session = Depends(get_db)):
    """
    Fetches all alarms that are ringing right now or are currently pending.
    In a real app, this would filter by 'alarm_time <= now'.
    """
    orders = db.query(Order).filter(Order.status.in_(["pending", "ringing"])).all()
    
    # Format the response for the mobile app
    result = []
    for order in orders:
        result.append({
            "order_id": order.id,
            "item_name": order.menu_item.name,
            "quantity": order.quantity,
            "serve_time": order.requested_serve_time,
            "status": order.status
        })
    return result

@router.post("/alarms/{order_id}/acknowledge")
def acknowledge_alarm(order_id: int, db: Session = Depends(get_db)):
    """
    Called by the Staff App when the staff taps 'Stop Alarm'.
    """
    order = db.query(Order).filter(Order.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.status = "acknowledged"
    db.commit()
    return {"message": "Alarm stopped. Kitchen is preparing the food."}