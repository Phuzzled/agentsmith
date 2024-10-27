"""
Simple example of using the computer-use project with Ollama.
"""
import asyncio
import json
from computer_use.loop import sampling_loop, APIProvider

async def main():
    # Example callback functions
    def output_callback(content):
        if content["type"] == "text":
            print(f"AI: {content['text']}")

    def tool_callback(result, tool_id):
        print(f"Tool {tool_id} output: {result.output if result.output else result.error}")

    def api_callback(request, response, error):
        if error:
            print(f"Error: {error}")

    # Example with default local Ollama
    await sampling_loop(
        provider=APIProvider.OLLAMA,
        messages=[{
            "role": "user",
            "content": "Hello! Could you help me test if this installation is working?"
        }],
        output_callback=output_callback,
        tool_output_callback=tool_callback,
        api_response_callback=api_callback,
        api_key="",
        system_prompt_suffix="You are a helpful AI assistant testing if the installation works correctly."
    )

    # Example with custom Ollama endpoint
    config = {
        "host": "localhost",  # Change this to your Ollama host if needed
        "port": 11434,
        "scheme": "http"
    }
    
    print("\nTesting with custom endpoint configuration...")
    await sampling_loop(
        provider=APIProvider.OLLAMA,
        messages=[{
            "role": "user",
            "content": "Can you confirm you're connected through a custom endpoint?"
        }],
        output_callback=output_callback,
        tool_output_callback=tool_callback,
        api_response_callback=api_callback,
        api_key=json.dumps(config),
        system_prompt_suffix="You are a helpful AI assistant testing custom endpoint configuration."
    )

if __name__ == "__main__":
    asyncio.run(main())