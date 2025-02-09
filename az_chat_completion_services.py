from enum import Enum
from typing import TYPE_CHECKING

from semantic_kernel.exceptions.service_exceptions import ServiceInitializationError

if TYPE_CHECKING:
    from semantic_kernel.connectors.ai.chat_completion_client_base import ChatCompletionClientBase
    from semantic_kernel.connectors.ai.prompt_execution_settings import PromptExecutionSettings

service_id = "azureopenai_chat_service"

def get_azure_openai_chat_completion_service_and_request_settings(
    instruction_role: str | None = None,
) -> tuple["ChatCompletionClientBase", "PromptExecutionSettings"]:
    """Return Azure OpenAI chat completion service and request settings.

    Args:
        instruction_role (str | None): The role to use for 'instruction' messages, for example,
            'developer' or 'system'. (Optional)
    """
    from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings

    # chat_service = AzureChatCompletion(service_id=service_id, instruction_role=instruction_role)
    
    chat_service = AzureChatCompletion(
        service_id=service_id,
        api_key="",
        deployment_name="gpt-35-turbo",
        endpoint="https://sk-azureopenai-sarvm.openai.azure.com/openai/deployments/gpt-35-turbo/chat/completions?api-version=2024-08-01-preview",
        base_url="https://sk-azureopenai-sarvm.openai.azure.com/openai", #semantic kernel sample won't work, this need to set to make it work '/openai' to be base url. 
        api_version="2024-08-01-preview",
        instruction_role="Cloud Expert"
    )

    request_settings = AzureChatPromptExecutionSettings(service_id=service_id)

    return chat_service, request_settings