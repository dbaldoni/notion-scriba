"""Google Gemini models provider."""

from typing import Optional
import google.generativeai as genai

from .base import BaseLLMProvider


class GoogleProvider(BaseLLMProvider):
    """Google Gemini models provider.
    
    Supports:
    - Gemini 1.5 Pro (best for complex tasks)
    - Gemini 1.5 Flash (faster, cost-effective)
    """
    
    def _initialize_client(self):
        """Initialize Google Generative AI client."""
        genai.configure(api_key=self.config.api_key)
        return genai.GenerativeModel(self.config.model)
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        """Generate text using Gemini.
        
        Args:
            prompt: User prompt
            system_prompt: Optional system instructions
            
        Returns:
            Generated text from Gemini
        """
        # Gemini doesn't have separate system prompt,
        # so we prepend it to the user prompt
        full_prompt = prompt
        if system_prompt:
            full_prompt = f"{system_prompt}\n\n{prompt}"
        
        generation_config = {
            "temperature": self.config.temperature,
            "max_output_tokens": self.config.max_tokens,
        }
        
        response = self.client.generate_content(
            full_prompt,
            generation_config=generation_config
        )
        
        return response.text
    
    def get_token_count(self, text: str) -> int:
        """Get token count using Gemini's tokenizer.
        
        Args:
            text: Input text
            
        Returns:
            Exact token count
        """
        try:
            return self.client.count_tokens(text).total_tokens
        except Exception:
            # Fallback approximation
            return len(text) // 4
    
    @property
    def provider_name(self) -> str:
        """Return provider name."""
        return "Google"
