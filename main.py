import json
import sys
from typing import Optional, Dict, Any
from datetime import datetime

import requests

try:
    import config
except ImportError:
    print("Error: config.py not found. Please create it from config.example.py")
    sys.exit(1)


class OpenRouterClient:
    BASE_URL = "https://openrouter.ai/api/v1/chat/completions"
    
    def __init__(
        self,
        api_key: str,
        model_name: str = "qwen/qwen-vl-plus",
        max_tokens: int = 2000,
        temperature: float = 0.8
    ):
        if not api_key:
            raise ValueError("API key is required")
        
        self.api_key = api_key
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature
    
    def _build_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://qodam.com",
            "X-Title": "Post Generator"
        }
    
    def _build_payload(self, prompt: str, url: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        content_list = [{"type": "text", "text": prompt}]
        
        if url:
            content_list.append({
                "type": "image_url",
                "image_url": {"url": url}
            })
        
        return {
            "model": kwargs.get("model", self.model_name),
            "messages": [
                {
                    "role": "user",
                    "content": content_list
                }
            ],
            "max_tokens": kwargs.get("max_tokens", self.max_tokens),
            "temperature": kwargs.get("temperature", self.temperature)
        }
    
    def generate(self, prompt: str, url: Optional[str] = None, verbose: bool = True, **kwargs) -> str:
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty")
        
        headers = self._build_headers()
        payload = self._build_payload(prompt, url, **kwargs)
        
        try:
            response = requests.post(
                self.BASE_URL,
                headers=headers,
                data=json.dumps(payload),
                timeout=60
            )
            response.raise_for_status()
            
            data = response.json()
            content = data["choices"][0]["message"]["content"].strip()
            
            if verbose:
                print(f"\n{'='*60}")
                print(f"Model: {self.model_name}")
                print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"{'='*60}\n")
                print(content)
                print(f"\n{'='*60}\n")
            
            return content
            
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}", file=sys.stderr)
            raise
        except (KeyError, IndexError) as e:
            print(f"Error parsing response: {e}", file=sys.stderr)
            raise


def main():
    try:
        client = OpenRouterClient(
            api_key=config.API_KEY_OPENROUTER,
            model_name="qwen/qwen-vl-plus"
        )
    except (AttributeError, ValueError) as e:
        print(f"Configuration error: {e}", file=sys.stderr)
        sys.exit(1)
    
    prompt = """Write a short, engaging social media post about the benefits of    
                learning to code in 2025. Keep it under 280 characters."""
    
    image_url = None  # Mettre l'URL ici si tu veux inclure une image
    
    try:
        response = client.generate(prompt, url=image_url)
        
        # Optionnel: sauvegarder dans un fichier
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # with open(f"output_{timestamp}.txt", "w", encoding="utf-8") as f:
        #     f.write(response)
        
    except Exception as e:
        print(f"Failed to generate response: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
