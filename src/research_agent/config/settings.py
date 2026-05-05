import os
from pydantic import BaseModel

class Settings(BaseModel):
    # API Keys
    AKASH_API_KEY: str = os.getenv("AKASH_API_KEY", "")
    
    # Model config
    MODEL_NAME: str = "minimax-m2.5"
    MAX_TOKENS: int = 8192
    
    # Database
    CHROMA_PERSIST_DIR: str = "./.chroma_db"
    
    # Processing
    MAX_WORKERS: int = 4
    
settings = Settings()