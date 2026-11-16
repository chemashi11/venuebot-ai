from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from app.core.database import get_db
from app.models.menu import MenuItem

router = APIRouter()

class MenuItemCreate(BaseModel):
    name: str
    category: str # drink, snack, meal
    prep_time_minutes: int
    price: float

class MenuItemResponse(BaseModel):
    id: int
    name: str
    category: str
    prep_time_minutes: int
    price: float
    is_available: bool

    class Config:
        from_attributes = True

@router.post("/", response_model=MenuItemResponse)
def create_menu_item(item: MenuItemCreate, db: Session = Depends(get_db)):
    db_item = MenuItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/", response_model=List[MenuItemResponse])
def get_menu(db: Session = Depends(get_db)):
    return db.query(MenuItem).all()