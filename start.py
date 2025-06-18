#! /bin/python
import uvicorn
from isagog_docs.core.config import settings
from isagog_docs.core.logging import LOGGING_CONFIG

if __name__ == "__main__":

    uvicorn.run("isagog_docs.main:app", 
                host = settings.APP_HOST, 
                port = settings.APP_PORT, 
                workers = settings.APP_WORKERS,
                log_config = LOGGING_CONFIG
            )