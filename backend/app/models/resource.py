from sqlalchemy import Column, Integer, String, Float, Boolean
from app.core.database import Base

class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False) # e.g., "Table 1", "Study Spot A", "Event Hall"
    type = Column(String, nullable=False) # types: table, hall, study_spot
    capacity = Column(Integer, nullable=False)
    is_loud_zone = Column(Boolean, default=False) # True for Event Hall
    base_price_per_hour = Column(Float, nullable=False)