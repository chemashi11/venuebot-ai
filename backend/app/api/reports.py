from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.reporting import generate_monthly_report
import datetime

router = APIRouter()

@router.get("/generate")
def create_report(month: int, year: int, db: Session = Depends(get_db)):
    file_path = generate_monthly_report(db, month, year)
    
    if file_path.endswith(".png"):
        # Return the actual image file
        return FileResponse(file_path, media_type="image/png", filename="report.png")
    else:
        return {"message": file_path}