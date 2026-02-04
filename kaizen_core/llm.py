"""
LLM Client for Kaizen Agent
Supports multiple providers with auto-detection from environment variables.

Providers (Feb 2026):
- OpenAI: gpt-5.2, gpt-5-mini, gpt-5-nano
- Anthropic: claude-opus-4.5, claude-sonnet-4.5, claude-haiku-4.5
- Google: gemini-3-pro-preview, gemini-3-pro, gemini-3-flash
- Ollama: local models (fallback)
"""
import json
import logging
import os
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Load .env file if it exists (for local development)
# Uses direct assignment to override system env vars
def _load_env_file():
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()

_load_env_file()

# Default models per provider (Feb 2026)
DEFAULT_MODELS = {
    "openai": "gpt-5-mini",           # Good balance of cost/quality
    "anthropic": "claude-sonnet-4.5", # Best for coding
    "google": "gemini-3-pro-preview", # User's preferred model
    "ollama": "llama3.2",             # Local fallback
}


def detect_provider() -> tuple[str, str | None]:
    """
    Auto-detect provider from environment variables.
    Returns: (provider_name, api_key)
    
    Priority can be overridden with KAIZEN_PROVIDER env var.
    Default: Google > OpenAI > Anthropic > Ollama (if Google key in .env)
    """
    # Allow explicit override
    if forced := os.environ.get("KAIZEN_PROVIDER"):
        forced = forced.lower()
        if forced == "google" and (key := os.environ.get("GOOGLE_API_KEY")):
            return "google", key
        if forced == "openai" and (key := os.environ.get("OPENAI_API_KEY")):
            return "openai", key
        if forced == "anthropic" and (key := os.environ.get("ANTHROPIC_API_KEY")):
            return "anthropic", key
        if forced == "ollama":
            return "ollama", None
    
    # Check .env-loaded Google key first (user preference)
    if key := os.environ.get("GOOGLE_API_KEY"):
        return "google", key
    if key := os.environ.get("GEMINI_API_KEY"):
        return "google", key
    if key := os.environ.get("OPENAI_API_KEY"):
        return "openai", key
    if key := os.environ.get("ANTHROPIC_API_KEY"):
        return "anthropic", key
    # Fallback to local Ollama
    return "ollama", None


class LLMClient:
    def __init__(
        self,
        provider: str | None = None,
        model: str | None = None,
        api_key: str | None = None,
        base_url: str = "http://localhost:11434"
    ):
        # Auto-detect if not specified
        if provider is None:
            provider, detected_key = detect_provider()
            if api_key is None:
                api_key = detected_key
        
        self.provider = provider
        self.model = model or DEFAULT_MODELS.get(provider, "gpt-5-mini")
        self.api_key = api_key
        self.base_url = base_url
        
        logging.info(f"LLM: Using {self.provider} with model {self.model}")
        
        if self.provider == "ollama":
            self._ensure_ollama_running()

    def _ensure_ollama_running(self):
        """Checks if Ollama is running, starts it, and ensures model exists."""
        logging.info("Checking Ollama health...")
        if not self._is_ollama_healthy():
            logging.warning("Ollama is offline. Starting server...")
            self._start_ollama_server()
        
        logging.info(f"Checking for model '{self.model}'...")
        if not self._has_ollama_model(self.model):
            logging.warning(f"Model '{self.model}' missing. Downloading...")
            self._pull_ollama_model(self.model)

    def _start_ollama_server(self):
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
                if self._is_ollama_healthy():
                    logging.info("Ollama started successfully.")
                    return
            logging.error("Failed to start Ollama (timed out).")
        except Exception as e:
            logging.error(f"Error starting Ollama: {e}")

    def _is_ollama_healthy(self) -> bool:
        try:
            with urllib.request.urlopen(f"{self.base_url}/api/tags", timeout=1) as response:
                return response.status == 200
        except Exception:
            return False

    def _has_ollama_model(self, model_name: str) -> bool:
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

    def _pull_ollama_model(self, model_name: str):
        url = f"{self.base_url}/api/pull"
        data = json.dumps({"name": model_name}).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        try:
            logging.info("Pulling model... (please wait)")
            with urllib.request.urlopen(req, timeout=600) as response:
                while response.read(1024):
                    pass
            logging.info("Model installed.")
        except Exception as e:
            logging.error(f"Failed to pull model: {e}")

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Generates a completion from the LLM."""
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        
        if self.provider == "ollama":
            return self._call_ollama(messages)
        elif self.provider == "openai":
            return self._call_openai(messages)
        elif self.provider == "anthropic":
            return self._call_anthropic(messages)
        elif self.provider == "google":
            return self._call_google(messages)
        else:
            raise NotImplementedError(f"Provider {self.provider} not implemented.")

    def _call_ollama(self, messages: list[dict]) -> str:
        url = f"{self.base_url}/api/chat"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": 0.2}
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["message"]["content"]
        except urllib.error.URLError as e:
            return f"Error connecting to Ollama: {e}"

    def _call_openai(self, messages: list[dict]) -> str:
        url = "https://api.openai.com/v1/chat/completions"
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.2
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            }
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["choices"][0]["message"]["content"]
        except urllib.error.URLError as e:
            return f"Error calling OpenAI: {e}"

    def _call_anthropic(self, messages: list[dict]) -> str:
        url = "https://api.anthropic.com/v1/messages"
        
        # Convert to Anthropic format
        system = next((m["content"] for m in messages if m["role"] == "system"), "")
        user_messages = [m for m in messages if m["role"] != "system"]
        
        payload = {
            "model": self.model,
            "max_tokens": 4096,
            "system": system,
            "messages": user_messages
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(
            url,
            data=data,
            headers={
                "Content-Type": "application/json",
                "x-api-key": self.api_key,
                "anthropic-version": "2024-01-01"
            }
        )
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["content"][0]["text"]
        except urllib.error.URLError as e:
            return f"Error calling Anthropic: {e}"

    def _call_google(self, messages: list[dict]) -> str:
        # Use Gemini API
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        
        # Convert to Gemini format
        parts = []
        for m in messages:
            parts.append({"text": f"{m['role'].upper()}: {m['content']}"})
        
        payload = {
            "contents": [{"parts": parts}],
            "generationConfig": {"temperature": 0.2}
        }
        
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        
        try:
            with urllib.request.urlopen(req) as response:
                result = json.loads(response.read().decode("utf-8"))
                return result["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.URLError as e:
            return f"Error calling Google: {e}"

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
            json_str = response.strip()
            if "```json" in json_str:
                json_str = json_str.split("```json")[1].split("```")[0].strip()
            elif "```" in json_str:
                json_str = json_str.split("```")[1].split("```")[0].strip()
            return json.loads(json_str)
        except Exception:
            return {"approved": True, "feedback": f"Warning: Could not parse Critic JSON. Raw: {response[:50]}"}


# Test
if __name__ == "__main__":
    client = LLMClient()
    print(client.complete("You are a helpful assistant.", "Say hello!"))
