from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not found in .env file")
    
    GA4_PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")

    GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL")
    GROQ_TEMPERATURE = float(os.getenv("GROQ_TEMPERATURE", 0.5))
    GROQ_MAX_TOKENS = int(os.getenv("GROQ_MAX_TOKENS", 2048))
    GROQ_TIMEOUT = int(os.getenv("GROQ_TIMEOUT", 60))