import os
from pydantic import ValidationError
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from custom_logger import setup_logger
import traceback

logger = setup_logger("Logger", log_file="validateopenai.log")

try:

    service = AzureChatCompletion(
        service_id="azureopenai_chat_service",
        api_key="CEudQGXQaHqpM1pgBXSK1O3fVIfmtpcI2KW2LwjradxR4t9sF3KLJQQJ99BBACHYHv6XJ3w3AAABACOGq667",
        deployment_name="gpt-35-turbo",
        endpoint="https://sk-azureopenai-sarvm.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview",
        base_url="https://sk-azureopenai-sarvm.openai.azure.com",
        api_version="2024-08-01-preview",
        instruction_role="Cloud Expert"
    )
    
    logger.info(f"success {service}")
except ValidationError as e:
    logger.error("An error occurred: %s", traceback.format_exc())
