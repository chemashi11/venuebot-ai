from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "VenueBot AI"
    DATABASE_URL: str = "postgresql://venuebot_admin:secretpassword@db:5432/venuebot_db"
    
    # Security settings
    SECRET_KEY: str = "super-secret-key-change-this-in-production" 
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7 

    # Email Settings
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = ""
    SMTP_PASSWORD: str = ""
    MANAGER_EMAIL: str = ""
    
    # AI Settings
    GROQ_API_KEY: str = "" 
    
    class Config:
        env_file = ".env"

settings = Settings()