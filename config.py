from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DATABASE_URL = os.getenv("DATABASE_URL")

    if not DATABASE_URL:
        raise ValueError("DATABASE_URL not found in .env file")
    
    GA4_PROPERTY_ID = os.getenv("GA4_PROPERTY_ID")

    GOOGLE_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")