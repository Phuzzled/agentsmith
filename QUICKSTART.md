# Quick Start Guide

This is a quick start guide to get you up and running with the computer-use project. For detailed instructions, please see INSTALL.md.

## Quick Installation

### Windows
1. Install Python 3.10+ from [Python.org](https://www.python.org/downloads/)
2. Install Ollama from [Ollama.ai](https://ollama.ai/download)
3. Open PowerShell and run:
```powershell
# Clone and install
git clone https://github.com/yourusername/computer-use.git
cd computer-use
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -e .
pip install -r computer_use/requirements.txt

# Pull the default Ollama model
ollama pull llama3.1:8b-instruct-q8_0
```

### Ubuntu
```bash
# Install Python and Git
sudo apt update && sudo apt install -y python3 python3-pip python3-venv git

# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Clone and install
git clone https://github.com/yourusername/computer-use.git
cd computer-use
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install -r computer_use/requirements.txt

# Pull the default Ollama model
ollama pull llama3.1:8b-instruct-q8_0
```

## Quick Usage Example

```python
from computer_use.loop import sampling_loop, APIProvider

# Using default local Ollama
await sampling_loop(
    provider=APIProvider.OLLAMA,
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    output_callback=print,
    tool_output_callback=lambda x, y: None,
    api_response_callback=lambda x, y, z: None,
    api_key=""
)
```

For more detailed setup instructions, configuration options, and troubleshooting, please refer to INSTALL.md.