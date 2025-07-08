

LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'custom_formatter': { 
            'format': "%(asctime)s [_pid: %(process)d] [_tid: %(thread)d] [%(levelname)s] [%(name)s] %(message)s"
            
        },
    },
    'handlers': { 
        'default': { 
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'stream_handler': { 
            'formatter': 'custom_formatter',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file_handler': { 
            'formatter': 'custom_formatter',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'app.log',
            'maxBytes': 1024 * 1024 * 1, # = 1MB
            'backupCount': 3,
        },
    },
    'loggers': { 
        'uvicorn': {
            'handlers': ['default', 'file_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'uvicorn.access': {
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'uvicorn.error': { 
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
        'uvicorn.asgi': {
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'root': {
            'handlers': ['stream_handler', 'file_handler'],
            'level': 'INFO',
        },
    },
}