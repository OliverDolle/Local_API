# Configuration file for different environments
from pydantic import BaseSettings
from functools import lru_cache
from typing import Optional
from dotenv import load_dotenv
import os

class Settings(BaseSettings):
    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/mydb.db")
    
    # JWT settings
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Advanced Blog API"
    
    # CORS settings
    BACKEND_CORS_ORIGINS: list = ["*"]
    
    # Email settings (for future use)
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[str] = None
    EMAILS_FROM_NAME: Optional[str] = None
    
    class Config:
        case_sensitive = True
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()