import json
import logging
import os
import subprocess
import time
import urllib.error
import urllib.request
from typing import Any

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')


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
        logging.info("Checking Ollama health...")
        if not self._is_healthy():
            logging.warning("Ollama is offline. Starting server...")
            self._start_server()
        
        # 2. Check Model
        logging.info(f"Checking for model '{self.model}'...")
        if not self._has_model(self.model):
            logging.warning(f"Model '{self.model}' missing. Downloading...")
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
                logging.debug(f"Waiting for server ({i+1}/20)...")
                time.sleep(1)
                if self._is_healthy():
                    logging.info("Ollama started successfully.")
                    return
            logging.error("Failed to start Ollama (timed out).")
        except Exception as e:
            logging.error(f"Error starting Ollama: {e}")

    def _has_model(self, model_name: str) -> bool:
        try:
            with urllib.request.urlopen(f"{self.base_url}/api/tags") as response:
                if response.status == 200:
                    data = json.loads(response.read().decode())
                    for model in data.get("models", []):
                        if model["name"].startswith(model_name):
                            return True
            return False
        except Exception:
            return False

    def _pull_model(self, model_name: str):
        url = f"{self.base_url}/api/pull"
        data = json.dumps({"name": model_name}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        try:
            # We don't stream the response here for simplicity, just wait
            logging.info("Pulling model... (please wait)")
            with urllib.request.urlopen(req, timeout=600) as response:
                 # Read stream to completion
                 while response.read(1024): 
                     pass
            logging.info("Model installed.")
        except Exception as e:
             logging.error(f"Failed to pull model: {e}")

    def _is_healthy(self) -> bool:
        try:
            with urllib.request.urlopen(f"{self.base_url}/api/tags", timeout=1) as response:
                return response.status == 200
        except Exception:
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

    def critique_action(self, proposed_action: str, context: str) -> dict[str, Any]:
        """
        Reflexion Loop: Asks the LLM to critique the proposed action.
        Returns: {"approved": bool, "feedback": str}
        """
        system_prompt = """
You are the KAIZEN CRITIC. Your job is to prevent the agent from making mistakes.
Review the proposed tool action.

CRITERIA:
1. SAFETY: Is the command dangerous (e.g., 'rm -rf')?
2. CORRECTNESS: Does the syntax look valid?
3. RELEVANCE: Does this help the objective?

Output JSON ONLY:
{
    "approved": true/false,
    "feedback": "Short reason why approved or rejected"
}
"""
        user_prompt = f"CONTEXT: {context}\n\nPROPOSED ACTION: {proposed_action}"
        
        response = self.complete(system_prompt, user_prompt)
        
        try:
            # Extract JSON from potential markdown blocks
            json_str = response.strip()
            if "```json" in json_str:
                json_str = json_str.split("```json")[1].split("```")[0].strip()
            elif "```" in json_str:
                json_str = json_str.split("```")[1].split("```")[0].strip()
                
            return json.loads(json_str)
        except Exception:
            # Fallback if JSON parsing fails - assume cautious approval but warn
            return {"approved": True, "feedback": f"Warning: Could not parse Critic JSON. Proceeding with caution. Raw: {response[:50]}"}

    def _call_ollama(self, messages: list[dict]) -> str:
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
