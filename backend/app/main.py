from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base
from app.models import User, Resource, MenuItem, Booking
from app.api import auth, agent, resources, menu, staff

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="VenueBot AI API",
    description="Backend for the VenueBot AI SaaS Platform",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(agent.router, prefix="/api/v1/agent", tags=["AI Agent"]) 
app.include_router(resources.router, prefix="/api/v1/resources", tags=["Resources (Owner)"]) 
app.include_router(menu.router, prefix="/api/v1/menu", tags=["Menu (Owner)"]) 
app.include_router(staff.router, prefix="/api/v1/staff", tags=["Staff Operations"])

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "VenueBot AI Backend"}