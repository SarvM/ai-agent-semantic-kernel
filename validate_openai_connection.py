import os
from pydantic import ValidationError
from az_chat_completion_services import get_azure_openai_chat_completion_service_and_request_settings
from custom_logger import setup_logger
import traceback

logger = setup_logger("Logger", log_file="validateopenai.log")

try:

    chat_completion_service, request_settings = get_azure_openai_chat_completion_service_and_request_settings()
    
    logger.info(f"success")
except ValidationError as e:
    logger.error("An error occurred: %s", traceback.format_exc())
