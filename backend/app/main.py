from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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

@app.get("/")
def read_root():
    return {"status": "healthy", "service": "VenueBot AI Backend"}

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok", "version": "0.1.0"}