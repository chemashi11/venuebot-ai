from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "VenueBot AI"
    DATABASE_URL: str = "postgresql://venuebot_admin:secretpassword@db:5432/venuebot_db"
    
    # Security settings for JWT
    SECRET_KEY: str = "super-secret-key-change-this-in-production" 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 # 7 days
    
    class Config:
        env_file = ".env"

settings = Settings()