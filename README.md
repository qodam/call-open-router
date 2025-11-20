# OpenRouter API Client

A clean, well-structured Python client for interacting with [OpenRouter](https://openrouter.ai/)'s AI models.

## Features

- 🚀 Simple and intuitive API
- 🔧 Configurable model parameters
- 📝 Detailed logging and error handling
- 🎯 Type hints for better IDE support
- ⚡ Timeout protection
- 🛡️ Comprehensive error handling
- 🖼️ Image input support (vision models)

## Requirements

- Python 3.7+
- `requests` library

## Installation

1. **Clone the repository**
```bash
   git clone https://github.com/qodam/call-open-router.git
   cd call-open-router
```

2. **Install dependencies**
```bash
   pip install -r requirements.txt
```

3. **Configure your API key**
```bash
   cp config.example.py config.py
```
   
   Edit `config.py` and add your OpenRouter API key:
```python
   API_KEY_OPENROUTER = "sk-or-v1-..."
```
   
   Get your API key from: https://openrouter.ai/keys

## Usage

### Basic Usage
```python
from main import OpenRouterClient

# Initialize the client
client = OpenRouterClient(
    api_key="your_api_key",
    model_name="qwen/qwen-vl-plus"
)

# Generate a response
response = client.generate("Write a haiku about coding")
print(response)
```

### Run the Example
```bash
python main.py
```

### Advanced Usage
```python
# Customize parameters per request
response = client.generate(
    prompt="Explain quantum computing",
    model="anthropic/claude-3-sonnet",
    max_tokens=1500,
    temperature=0.5,
    verbose=False  # Disable console output
)

# Use with image input (vision models)
response = client.generate(
    prompt="Describe this image in detail",
    url="https://example.com/image.jpg",
    model="qwen/qwen-vl-plus"
)
```

## Configuration

The `OpenRouterClient` accepts the following parameters:

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `api_key` | str | Required | Your OpenRouter API key |
| `model_name` | str | `"qwen/qwen-vl-plus"` | Model to use |
| `max_tokens` | int | `2000` | Maximum response length |
| `temperature` | float | `0.8` | Sampling temperature (0-2) |

### generate() Method Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `prompt` | str | Required | Your text prompt |
| `url` | str | None | Optional image URL for vision models |
| `verbose` | bool | True | Print formatted output to console |
| `**kwargs` | dict | - | Override model, max_tokens, temperature |

## Available Models

OpenRouter supports many models. Popular choices include:

- `qwen/qwen-vl-plus` - Vision-language model
- `anthropic/claude-3-opus` - Most capable Claude model
- `anthropic/claude-3-sonnet` - Balanced performance
- `openai/gpt-4-turbo` - Latest GPT-4
- `google/gemini-pro` - Google's Gemini

See the full list at: https://openrouter.ai/models

## Project Structure
```
openrouter-client/
│
├── main.py              # Main client implementation
├── config.example.py    # Configuration template
├── config.py            # Your API key (gitignored)
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Error Handling

The client includes comprehensive error handling:
```python
try:
    response = client.generate("Your prompt")
except ValueError as e:
    print(f"Invalid input: {e}")
except requests.HTTPError as e:
    print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

## Security Notes

- ⚠️ **Never commit `config.py` to version control**
- ⚠️ **Never share your API key publicly**
- ⚠️ **Use environment variables in production**

### Using Environment Variables

For production environments:
```python
import os

client = OpenRouterClient(
    api_key=os.environ.get("OPENROUTER_API_KEY")
)
```

## Example Output
```
============================================================
Model: qwen/qwen-vl-plus
Timestamp: 2025-11-20 14:30:45
============================================================

🚀 2025 is the perfect time to learn coding! Whether you're 
building AI apps, automating tasks, or launching a startup, 
coding unlocks endless possibilities. Start your journey today! 
💻✨ #LearnToCode #TechSkills

============================================================
```

## Roadmap

- [x] Add image input support
- [ ] Add async support
- [ ] Implement streaming responses
- [ ] Add conversation history management
- [ ] Create CLI interface
- [ ] Add unit tests
- [ ] Support for multiple images

## Acknowledgments

- [OpenRouter](https://openrouter.ai/) for providing the API
- Built with Python and ❤️

---

**Made with 🤖 by QODAM**
