"""Ollama client integration for the Data Engineering Copilot."""

import os
from typing import Any, Dict, List, Optional

import ollama
from langchain.llms import Ollama
from rich.console import Console

console = Console()


class OllamaClient:
    """Client for interacting with Ollama models."""

    def __init__(self, model: Optional[str] = None, base_url: Optional[str] = None):
        """Initialize the Ollama client.
        
        Args:
            model: Model name to use (defaults to env var OLLAMA_MODEL)
            base_url: Ollama base URL (defaults to env var OLLAMA_BASE_URL)
        """
        self.model = model or os.getenv("OLLAMA_MODEL", "codellama:7b")
        self.fallback_model = os.getenv("OLLAMA_FALLBACK_MODEL", "mistral:7b")
        self.base_url = base_url or os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        # Configure ollama client
        ollama.set_host(self.base_url)
        
        # Initialize LangChain Ollama
        self.llm = Ollama(
            model=self.model,
            base_url=self.base_url,
            temperature=0.1,
        )
        
        console.print(f"[green]Initialized Ollama client with model: {self.model}[/green]")

    def generate(self, prompt: str, model: Optional[str] = None) -> str:
        """Generate text using the specified model.
        
        Args:
            prompt: The prompt to send to the model
            model: Optional model override
            
        Returns:
            Generated text response
        """
        try:
            if model:
                # Use specific model for this request
                temp_llm = Ollama(
                    model=model,
                    base_url=self.base_url,
                    temperature=0.1,
                )
                response = temp_llm.invoke(prompt)
            else:
                response = self.llm.invoke(prompt)
            
            return response.strip()
            
        except Exception as e:
            console.print(f"[red]Error with model {model or self.model}: {e}[/red]")
            
            # Try fallback model
            if model != self.fallback_model:
                console.print(f"[yellow]Trying fallback model: {self.fallback_model}[/yellow]")
                return self.generate(prompt, self.fallback_model)
            
            raise

    def list_models(self) -> List[Dict[str, Any]]:
        """List available models.
        
        Returns:
            List of available models
        """
        try:
            models = ollama.list()
            return models.get("models", [])
        except Exception as e:
            console.print(f"[red]Error listing models: {e}[/red]")
            return []

    def is_model_available(self, model: str) -> bool:
        """Check if a model is available.
        
        Args:
            model: Model name to check
            
        Returns:
            True if model is available
        """
        models = self.list_models()
        return any(m["name"] == model for m in models)

    def health_check(self) -> bool:
        """Check if Ollama is running and accessible.
        
        Returns:
            True if healthy
        """
        try:
            models = self.list_models()
            return len(models) > 0
        except Exception:
            return False
