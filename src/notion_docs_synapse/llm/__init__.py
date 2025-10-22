"""
LLM Provider abstraction layer.

Supports multiple AI providers:
- OpenAI (GPT-4, GPT-4o, GPT-3.5-turbo)
- Anthropic (Claude 3.5 Sonnet, Opus, Haiku)
- Google (Gemini 1.5 Pro, Flash)
- DeepSeek (DeepSeek Chat, Coder)
- Ollama (Local models: Llama, Mistral, etc.)
"""

from .base import BaseLLMProvider, LLMConfig
from .factory import LLMProviderFactory

__all__ = ["BaseLLMProvider", "LLMConfig", "LLMProviderFactory"]
