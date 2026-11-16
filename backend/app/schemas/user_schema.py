from pydantic import BaseModel, EmailStr, field_validator
import re

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: str = "customer"

    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, v: str) -> str:
        # Check if the email ends with @gmail.com (case-insensitive)
        if not v.lower().endswith("@gmail.com"):
            raise ValueError("Email must be a @gmail.com address")
        return v.lower() # Save emails in lowercase to prevent duplicates

    @field_validator('password')
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain at least one uppercase letter")
        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain at least one lowercase letter")
        if not re.search(r"\d", v):
            raise ValueError("Password must contain at least one number")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain at least one special symbol")
        return v

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str