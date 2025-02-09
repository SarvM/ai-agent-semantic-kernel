import asyncio
from custom_logger import setup_logger
from az_chat_completion_services import get_azure_openai_chat_completion_service_and_request_settings
from semantic_kernel.contents import ChatHistory

logger = setup_logger("Logger", log_file="azchatcompletion.log")

chat_completion_service, request_settings = get_azure_openai_chat_completion_service_and_request_settings()

system_message = """
You are a chat bot. Your name is Jackal and
you have one goal: figure out what people need.
Your full name, should you need to know it, is
Jackal. You communicate
effectively, but you tend to answer with long
flowery prose.
"""

chat_history = ChatHistory(system_message=system_message)

async def chat() -> bool:
    try:
        try:
            user_input = input("User:> ")
        except KeyboardInterrupt:
            print("\n\nExiting chat...")
            return False
        except EOFError:
            print("\n\nExiting chat...")
            return False

        if user_input == "exit":
            print("\n\nExiting chat...")
            return False
        
        # Add the user message to the chat history so that the chatbot can respond to it.
        chat_history.add_user_message(user_input)
        
        # Get the chat message content from the chat completion service.
        response = await chat_completion_service.get_chat_message_content(
            chat_history=chat_history,
            settings=request_settings,
        )
        if response:
            print(f"Jackal:> {response}")

            # Add the chat message to the chat history to keep track of the conversation.
            chat_history.add_message(response)
    
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)  # Log exception with traceback
    
    return True

async def main() -> None:
    chatting = True
    while chatting:
        chatting = await chat()

if __name__ == "__main__":
    asyncio.run(main())