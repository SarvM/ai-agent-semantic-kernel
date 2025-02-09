import logging
import os
from logging.handlers import RotatingFileHandler

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger(name, log_file="app.log", level=logging.DEBUG):
    """
    Create a logger instance with file and console handlers.
    
    :param name: Name of the logger
    :param log_file: Log file name (placed inside logs directory)
    :param level: Logging level
    :return: Configured logger instance
    """
    log_path = os.path.join(LOG_DIR, log_file)  # Store logs in "logs" folder
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate logs
    if logger.hasHandlers():
        return logger

    # Log format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    # File handler with rotation
    file_handler = RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=5)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.INFO)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
