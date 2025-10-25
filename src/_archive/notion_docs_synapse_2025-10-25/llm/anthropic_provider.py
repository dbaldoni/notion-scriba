"""Anthropic Claude models provider."""

from typing import Optional
from anthropic import Anthropic

from .base import BaseLLMProvider


class AnthropicProvider(BaseLLMProvider):
    """Anthropic Claude models provider.
    
    Supports:
    - Claude 3.5 Sonnet (best balance)
    - Claude 3 Opus (most capable)
    - Claude 3 Haiku (fastest, cheapest)
    """
    
    def _initialize_client(self):
        """Initialize Anthropic client."""
        return Anthropic(api_key=self.config.api_key)
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate text using Claude.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system instructions
            
        Returns:
            Generated text from Claude
        """
        response = self.client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system=system_prompt or "",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.content[0].text
    
    def get_token_count(self, text: str) -> int:
        """Estimate token count.
        
        Note: Anthropic doesn't provide a public tokenizer,
        so we use an approximation similar to GPT models.
        
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
        return "Anthropic"
