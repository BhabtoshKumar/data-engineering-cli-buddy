#!/bin/bash

# Data Engineering CLI Copilot Installation Script

set -e

echo "🤖 Installing Data Engineering CLI Copilot..."

# Check if Python 3.8+ is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check Python version
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python 3.8+ is required. Found: $python_version"
    exit 1
fi

echo "✅ Python $python_version found"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is required but not installed."
    exit 1
fi

echo "✅ pip3 found"

# Install the package in development mode
echo "📦 Installing package in development mode..."
pip3 install -e .

# Copy environment template
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp env.example .env
    echo "✅ Created .env file. Please configure it with your settings."
else
    echo "✅ .env file already exists"
fi

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "⚠️  Ollama is not installed. Please install it from https://ollama.ai"
    echo "   After installation, run:"
    echo "   ollama pull codellama:7b"
    echo "   ollama pull mistral:7b"
else
    echo "✅ Ollama found"
fi

echo ""
echo "🎉 Installation complete!"
echo ""
echo "Next steps:"
echo "1. Install Ollama: https://ollama.ai"
echo "2. Pull required models:"
echo "   ollama pull codellama:7b"
echo "   ollama pull mistral:7b"
echo "3. Configure .env file with your settings"
echo "4. Test the CLI:"
echo "   copilot --help"
echo "   copilot setup"
echo ""
echo "Happy data engineering! 🚀"
