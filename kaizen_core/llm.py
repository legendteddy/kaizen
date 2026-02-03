import json
import os
import urllib.request
import urllib.error
from typing import List, Dict, Optional

class LLMClient:
    def __init__(self, provider="ollama", model="llama3", base_url="http://localhost:11434"):
        self.provider = provider
        self.model = model
        self.base_url = base_url

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Generates a completion from the LLM."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        if self.provider == "ollama":
            return self._call_ollama(messages)
        else:
            raise NotImplementedError(f"Provider {self.provider} not implemented yet.")

    def _call_ollama(self, messages: List[Dict]) -> str:
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {
                "temperature": 0.2
            }
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["message"]["content"]
        except urllib.error.URLError as e:
            return f"Error connecting to Ollama: {e}"

# Test
if __name__ == "__main__":
    client = LLMClient()
    print(client.complete("You are a helpful assistant.", "Say hello!"))
