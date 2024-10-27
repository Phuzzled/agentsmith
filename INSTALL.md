# Installation Instructions

This guide provides instructions for installing and setting up the computer-use project on both Windows and Ubuntu systems.

## Prerequisites

### Windows Prerequisites
1. Install Python 3.10 or later
   - Download from [Python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"

2. Install Git
   - Download from [Git-scm.com](https://git-scm.com/download/windows)
   - Use default installation options

3. Install Ollama (Optional - if using Ollama AI provider)
   - Download from [Ollama.ai](https://ollama.ai/download)
   - Follow the installation wizard
   - After installation, open PowerShell and run:
     ```powershell
     ollama pull llama3.1:8b-instruct-q8_0
     ```

### Ubuntu Prerequisites
1. Install Python 3.10 or later and Git
   ```bash
   sudo apt update
   sudo apt install -y python3 python3-pip python3-venv git
   ```

2. Install Ollama (Optional - if using Ollama AI provider)
   ```bash
   curl -fsSL https://ollama.ai/install.sh | sh
   ollama pull llama3.1:8b-instruct-q8_0
   ```

## Installation Steps

### Windows Installation
1. Open PowerShell and clone the repository:
   ```powershell
   git clone https://github.com/yourusername/computer-use.git
   cd computer-use
   ```

2. Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install the project:
   ```powershell
   pip install -e .
   pip install -r computer_use/requirements.txt
   pip install -r dev-requirements.txt
   ```

### Ubuntu Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/computer-use.git
   cd computer-use
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the project:
   ```bash
   pip install -e .
   pip install -r computer_use/requirements.txt
   pip install -r dev-requirements.txt
   ```

## Configuration

### Environment Variables
Create a `.env` file in the project root directory:

```ini
# Required for Anthropic API (if using Claude)
ANTHROPIC_API_KEY=your_api_key_here

# Optional: Custom Ollama endpoint (if not using default localhost:11434)
OLLAMA_HOST=localhost
OLLAMA_PORT=11434
OLLAMA_SCHEME=http
```

## Verify Installation

To verify the installation is working correctly:

### Windows
```powershell
# Activate virtual environment if not already activated
.\venv\Scripts\Activate.ps1

# Run a test command
python -c "from computer_use.loop import APIProvider; print(APIProvider.OLLAMA.value)"
```

### Ubuntu
```bash
# Activate virtual environment if not already activated
source venv/bin/activate

# Run a test command
python3 -c "from computer_use.loop import APIProvider; print(APIProvider.OLLAMA.value)"
```

Expected output: `ollama`

## Using with Different AI Providers

### Ollama
1. Start the Ollama service:
   - Windows: It runs as a service automatically after installation
   - Ubuntu: Just run `ollama serve` in a terminal

2. Test the connection:
   ```python
   from computer_use.loop import sampling_loop, APIProvider
   import json

   # Using default localhost setup
   await sampling_loop(
       provider=APIProvider.OLLAMA,
       # other parameters...
   )

   # Using custom endpoint
   config = {
       "host": "your_ollama_host",
       "port": 11434,
       "scheme": "http"
   }
   await sampling_loop(
       provider=APIProvider.OLLAMA,
       api_key=json.dumps(config),
       # other parameters...
   )
   ```

### Anthropic (Claude)
1. Set your API key in the `.env` file or environment variables
2. Use the ANTHROPIC provider in your code:
   ```python
   await sampling_loop(
       provider=APIProvider.ANTHROPIC,
       api_key="your_api_key_here",
       # other parameters...
   )
   ```

## Troubleshooting

### Common Issues

1. **"ollama command not found"**
   - Windows: Restart your computer after installing Ollama
   - Ubuntu: Make sure you've run the installation script and added Ollama to your PATH

2. **"Module not found" errors**
   - Ensure you're in the virtual environment
   - Try reinstalling requirements: `pip install -r computer_use/requirements.txt`

3. **Ollama connection errors**
   - Verify Ollama is running: 
     - Windows: Check Services app for "Ollama" service
     - Ubuntu: Run `ps aux | grep ollama`
   - Test with: `curl http://localhost:11434/api/version`

### Getting Help
- Open an issue on the GitHub repository
- Check existing issues for similar problems and solutions
- Include your OS, Python version, and error messages when reporting issues

## Updating

To update to the latest version:

```bash
git pull origin main
pip install -r computer_use/requirements.txt
```