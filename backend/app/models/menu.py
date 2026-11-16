from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False) # e.g., "Latte", "Sandwich"
    category = Column(String, nullable=False) # drink, snack, meal
    prep_time_minutes = Column(Integer, nullable=False) # Used for staff alarms!
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)