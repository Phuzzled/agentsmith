# Examples

This directory contains example scripts demonstrating how to use the computer-use project.

## Available Examples

### simple_chat.py
A basic example showing how to:
- Set up and use the default local Ollama endpoint
- Configure and use a custom Ollama endpoint
- Handle callbacks for output, tool usage, and API responses

To run the example:
```bash
# Make sure your virtual environment is activated
python examples/simple_chat.py
```

## Creating Your Own Examples

When creating your own scripts, remember to:
1. Import the necessary components from computer_use.loop
2. Set up appropriate callback functions
3. Configure the AI provider (Ollama, Anthropic, etc.)
4. Handle the async nature of the sampling_loop function

See the existing examples for patterns and best practices.