import os
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

class Settings:
    """Application configuration"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    BING_SEARCH_API_KEY = os.getenv("BING_SEARCH_API_KEY")
    BING_SEARCH_URL = os.getenv("BING_SEARCH_URL", "https://api.bing.microsoft.com/v7.0/search")
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/healthcare_db")
    MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
    
    # Vector Store
    FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "./data/faiss_index")
    
    # LLM Configuration
    LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))
    MAX_TOKENS = int(os.getenv("MAX_TOKENS", "2000"))
    
    # Redis
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    
    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "./logs/app.log")
    
    # Frontend
    STREAMLIT_THEME = os.getenv("STREAMLIT_THEME", "light")
    
    class Config:
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    return Settings()
