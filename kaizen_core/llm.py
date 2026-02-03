import json
import os
import time
import subprocess
import urllib.request
import urllib.error
from typing import List, Dict, Optional

class LLMClient:
    def __init__(self, provider="ollama", model="llama3.2", base_url="http://localhost:11434"):
        self.provider = provider
        self.model = model
        self.base_url = base_url
        
        if self.provider == "ollama":
            self._ensure_ollama_running()

    def _ensure_ollama_running(self):
        """Checks if Ollama is running, starts it, and ensures model exists."""
        # 1. Start Server
        print("❤️ Checking AI Pulse (Ollama)...")
        if not self._is_healthy():
            print("⚠️ AI is offline. Attempting to defibrillate (ollama serve)...")
            self._start_server()
        
        # 2. Check Model
        print(f"🧠 Checking for model '{self.model}'...")
        if not self._has_model(self.model):
            print(f"📉 Model '{self.model}' missing. Downloading (this may take a while)...")
            self._pull_model(self.model)

    def _start_server(self):
        # Resolve executable path
        ollama_bin = "ollama"
        if os.name == 'nt':
            user_path = os.path.join(os.environ.get("LOCALAPPDATA", ""), "Programs", "Ollama", "ollama.exe")
            if os.path.exists(user_path):
                ollama_bin = user_path

        try:
            subprocess.Popen(
                [ollama_bin, "serve"], 
                stdout=subprocess.DEVNULL, 
                stderr=subprocess.DEVNULL,
                creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == 'nt' else 0
            )
            for i in range(20):
                print(f"   Waiting for AI heartbeat ({i+1}/20)...")
                time.sleep(1)
                if self._is_healthy():
                    print("✅ AI successfully resurrected!")
                    return
            print("❌ Failed to start Ollama (Timed out).")
        except Exception as e:
            print(f"❌ Error starting Ollama: {e}")

    def _has_model(self, model_name: str) -> bool:
        try:
            with urllib.request.urlopen(f"{self.base_url}/api/tags") as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    for model in data.get("models", []):
                        if model["name"].startswith(model_name):
                            return True
            return False
        except:
            return False

    def _pull_model(self, model_name: str):
        url = f"{self.base_url}/api/pull"
        data = json.dumps({"name": model_name}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        try:
            # We don't stream the response here for simplicity, just wait
            print("   Pulling... (please wait)")
            with urllib.request.urlopen(req, timeout=600) as response:
                 # Read stream to completion
                 while response.read(1024): 
                     pass
            print("✅ Model installed.")
        except Exception as e:
             print(f"❌ Failed to pull model: {e}")

    def _is_healthy(self) -> bool:
        try:
            with urllib.request.urlopen(f"{self.base_url}/api/tags", timeout=1) as response:
                return response.status == 200
        except:
            return False

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Generates a completion from the LLM."""
        if self.provider == "ollama" and not self._is_healthy():
             self._ensure_ollama_running()

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
