#! /bin/python
import uvicorn
import os

from isagog_docs.core.config import Config
from isagog_docs.core.logging import LOGGING_CONFIG


# Override settings for development
settings = Config()

settings.MONGO_DB = "dev"
settings.MONGO_COLLECTION = "dev-collection" 
settings.OPENROUTER_MODEL = "google/gemini-2.0-flash-001"
settings.UPLOAD_DIR = "./uploads"

# Override logging config for development
LOGGING_CONFIG['loggers']['isagog_docs.main'] = {
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'TRACE',
            'propagate': False
        }
LOGGING_CONFIG['loggers']['isagog_docs.services.analysis'] = {
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'DEBUG',
            'propagate': False
        }

LOGGING_CONFIG['loggers']['isagog_docs.services.documents'] = { 
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'DEBUG',
            'propagate': False
        }

if __name__ == "__main__":

    uvicorn.run("isagog_docs.main:app", 
                host = "0.0.0.0", 
                port = 8000,
                reload = True,
                log_config = LOGGING_CONFIG
            )