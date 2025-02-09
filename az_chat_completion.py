import asyncio

from custom_logger import setup_logger
from az_chat_completion_services import get_azure_openai_chat_completion_service_and_request_settings

from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import KernelArguments

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

kernel = Kernel()

chat_function = kernel.add_function(
    plugin_name="ChatBot",
    function_name="Chat",
    prompt="{{$chat_history}}{{$user_input}}",
    template_format="semantic-kernel",
)

# Invoking a kernel function requires a service, so we add the chat completion service to the kernel.
kernel.add_service(chat_completion_service)

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
        
        # A:: Directly invoking the service 
        # # Add the user message to the chat history so that the chatbot can respond to it.
        # chat_history.add_user_message(user_input)
        
        # # Get the chat message content from the chat completion service.
        # response = await chat_completion_service.get_chat_message_content(
        #     chat_history=chat_history,
        #     settings=request_settings,
        # )
        # A::

        # Get the chat message content from the chat completion service.
        kernel_arguments = KernelArguments(
            settings=request_settings,
            chat_history=chat_history,
            user_input=user_input,
        )

        answer = await kernel.invoke(plugin_name="ChatBot", function_name="Chat", arguments=kernel_arguments)
        # Alternatively, you can invoke the function directly with the kernel as an argument:
        # answer = await chat_function.invoke(kernel, kernel_arguments)

        if answer:
            print(f"Jackal:> {answer}")

            # Since the user_input is rendered by the template, it is not yet part of the chat history, so we add it here.
            chat_history.add_user_message(user_input)
            # Add the chat message to the chat history to keep track of the conversation.
            chat_history.add_message(answer.value[0])
    
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)  # Log exception with traceback
    
    return True

async def main() -> None:
    chatting = True
    while chatting:
        chatting = await chat()

    # Sample Input:
    # User:> Why is the sky blue in one sentence?

if __name__ == "__main__":
    asyncio.run(main())