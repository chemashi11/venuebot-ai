from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from app.core.database import get_db
from app.models.resource import Resource

router = APIRouter()

class ResourceCreate(BaseModel):
    name: str
    type: str # table, hall, study_spot
    capacity: int
    is_loud_zone: bool = False
    base_price_per_hour: float

class ResourceResponse(BaseModel):
    id: int
    name: str
    type: str
    capacity: int
    is_loud_zone: bool
    base_price_per_hour: float

    class Config:
        from_attributes = True

@router.post("/", response_model=ResourceResponse)
def create_resource(resource: ResourceCreate, db: Session = Depends(get_db)):
    db_resource = Resource(**resource.model_dump())
    db.add(db_resource)
    db.commit()
    db.refresh(db_resource)
    return db_resource

@router.get("/", response_model=List[ResourceResponse])
def get_resources(db: Session = Depends(get_db)):
    return db.query(Resource).all()