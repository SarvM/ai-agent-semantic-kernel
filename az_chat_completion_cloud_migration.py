import asyncio

from custom_logger import setup_logger
from az_chat_completion_services import get_azure_openai_chat_completion_service_and_request_settings
from functools import reduce

from semantic_kernel import Kernel
from semantic_kernel.contents import ChatHistory, StreamingChatMessageContent
from semantic_kernel.functions import KernelArguments

logger = setup_logger("Logger", log_file="azchatcompletioncloudmigration.log")

chat_completion_service, request_settings = get_azure_openai_chat_completion_service_and_request_settings()

system_message = """
You are a highly experienced Cloud Migration Expert with deep expertise in designing and implementing cloud migration strategies. 
Your knowledge spans across major cloud providers (AWS, Azure, GCP) and best practices for lift-and-shift, re-platforming, and modernization.
You specialize in assessing on-premise infrastructure, defining optimal target state architectures, and ensuring security, scalability, and cost-efficiency. 
Your goal is to provide precise, actionable recommendations for a seamless and efficient migration.
"""

chat_history = ChatHistory(system_message=system_message)

kernel = Kernel()

chat_function = kernel.add_function(
    plugin_name="ChatBot",
    function_name="Chat",
    prompt="{{$chat_history}}{{$user_input}}",
    template_format="semantic-kernel",
)

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
        
        kernel_arguments = KernelArguments(
            settings=request_settings,
            chat_history=chat_history,
            user_input=user_input,
        )


        answer = kernel.invoke_stream(plugin_name="ChatBot", function_name="Chat", arguments=kernel_arguments)

        streamed_chunks: list[StreamingChatMessageContent] = []
        print("Cloud Expert Agent:> ", end="")
        async for message in answer:
            if isinstance(message[0], StreamingChatMessageContent):
                streamed_chunks.append(message[0])
            print(str(message[0]), end="")
        print("")

        chat_history.add_user_message(user_input)
        if streamed_chunks:
            streaming_chat_message = reduce(lambda first, second: first + second, streamed_chunks)
            chat_history.add_message(streaming_chat_message)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    except Exception as e:
        logger.error("Exception occurred", exc_info=True)  # Log exception with traceback
    
    return True

async def main() -> None:
    chatting = True
    while chatting:
        chatting = await chat()

    # Sample Input:
    # User:> What is cloud discovery and assessment?

if __name__ == "__main__":
    asyncio.run(main())