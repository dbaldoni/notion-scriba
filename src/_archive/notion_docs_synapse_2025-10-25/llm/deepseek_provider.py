"""DeepSeek models provider."""

from typing import Optional
from openai import OpenAI

from .base import BaseLLMProvider


class DeepSeekProvider(BaseLLMProvider):
    """DeepSeek models provider.
    
    DeepSeek uses OpenAI-compatible API, making integration simple.
    
    Supports:
    - deepseek-chat (general purpose, very cost-effective)
    - deepseek-coder (specialized for code tasks)
    """
    
    def _initialize_client(self):
        """Initialize DeepSeek client using OpenAI compatibility."""
        return OpenAI(
            api_key=self.config.api_key,
            base_url="https://api.deepseek.com"
        )
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate text using DeepSeek.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system instructions
            
        Returns:
            Generated text from DeepSeek
        """
        messages = []
        
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        
        messages.append({"role": "user", "content": prompt})
        
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=messages,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens
        )
        
        return response.choices[0].message.content
    
    def get_token_count(self, text: str) -> int:
        """Estimate token count.
        
        DeepSeek doesn't provide public tokenizer,
        using standard approximation.
        
        Args:
            text: Input text
            
        Returns:
            Estimated token count
        """
        # Approximation: ~4 characters per token
        return len(text) // 4
    
    @property
    def provider_name(self) -> str:
        """Return provider name."""
        return "DeepSeek"
