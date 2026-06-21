import logging
import logging.handlers
import os
from src.utils.config import get_settings

settings = get_settings()

# Create logs directory
os.makedirs(os.path.dirname(settings.LOG_FILE), exist_ok=True)

# Configure logging
logger = logging.getLogger("healthcare_assistant")
logger.setLevel(getattr(logging, settings.LOG_LEVEL))

# File handler
file_handler = logging.handlers.RotatingFileHandler(
    settings.LOG_FILE,
    maxBytes=10485760,  # 10MB
    backupCount=10
)
file_handler.setLevel(getattr(logging, settings.LOG_LEVEL))

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(getattr(logging, settings.LOG_LEVEL))

# Formatter
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
