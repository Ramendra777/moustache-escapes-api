import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = "Moustache Escapes API"
    DEBUG: bool = os.getenv("DEBUG", "False") == "True"
    GEOCODING_TIMEOUT: int = int(os.getenv("GEOCODING_TIMEOUT", "5"))
    MAX_DISTANCE_KM: int = int(os.getenv("MAX_DISTANCE_KM", "50"))

settings = Settings()