# Docker Setup Guide

This guide explains how to run the computer-use project using Docker, which provides a complete environment including Ollama AI support.

## Prerequisites

- Docker installed on your system
- Docker Compose (optional, but recommended)
- Git to clone the repository

## Quick Start

### Using Docker Compose (Recommended)

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/computer-use.git
   cd computer-use
   ```

2. Build and run:
   ```bash
   docker-compose up --build
   ```

### Using Docker Directly

1. Build the image:
   ```bash
   docker build -t computer-use-ollama -f Dockerfile.ollama .
   ```

2. Run the container:
   ```bash
   docker run -it --rm computer-use-ollama
   ```

## Usage Options

### Run Interactive Shell
```bash
docker run -it --rm computer-use-ollama /bin/bash
```

### Run Example Script
```bash
docker run -it --rm computer-use-ollama python examples/simple_chat.py
```

### Run with Custom Ollama Configuration
```bash
docker run -it --rm \
  -e OLLAMA_HOST=host.docker.internal \
  -e OLLAMA_PORT=11434 \
  -e OLLAMA_SCHEME=http \
  computer-use-ollama
```

## GPU Support

To enable GPU support:

1. Ensure you have NVIDIA Docker support installed
2. Uncomment the GPU section in docker-compose.yml
3. Run with:
   ```bash
   docker-compose up --build
   ```

Or with Docker directly:
```bash
docker run -it --rm --gpus all computer-use-ollama
```

## Development

To develop while running in Docker:

1. Mount your local code:
   ```bash
   docker run -it --rm \
     -v $(pwd)/examples:/app/examples \
     computer-use-ollama
   ```

2. Or use Docker Compose (already configured in docker-compose.yml)

## Troubleshooting

### Common Issues

1. **Ollama not starting:**
   - Check logs: `docker logs <container_id>`
   - Ensure port 11434 is not in use
   - Try increasing sleep time in start.sh

2. **GPU not detected:**
   - Verify NVIDIA Docker installation
   - Check GPU drivers
   - Run `nvidia-smi` on host

3. **Display issues:**
   - Verify Xvfb is running: `ps aux | grep Xvfb`
   - Check DISPLAY environment variable
   - Try restarting the container

### Getting Logs
```bash
# For Docker Compose
docker-compose logs

# For Docker
docker logs <container_id>
```

## Configuration

### Environment Variables

- `DISPLAY`: X11 display number (default: :1)
- `OLLAMA_HOST`: Ollama API host
- `OLLAMA_PORT`: Ollama API port
- `OLLAMA_SCHEME`: HTTP scheme for Ollama API

### Volumes

The Docker setup includes these volume mounts:
- `/app/examples`: For development and custom examples
- `/root/.ollama`: Persists Ollama models and config

## Updating

To update to the latest version:

1. Pull the latest code:
   ```bash
   git pull origin main
   ```

2. Rebuild the Docker image:
   ```bash
   docker-compose build
   # or
   docker build -t computer-use-ollama -f Dockerfile.ollama .
   ```