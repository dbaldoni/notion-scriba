"""
Notion Scriba - AI-powered bilingual documentation generator for Notion.

A modular system for automatic bilingual documentation generation with support
for multiple LLM providers and direct Notion synchronization.

"Verba volant, scripta manent" - Spoken words fly away, written words remain.
"""

__version__ = "1.0.0"

# Core components
from .llm import LLMProviderFactory, BaseLLMProvider, LLMConfig
from .code_analyzer import CodeAnalyzer
from .templates import DocumentationTemplates
from .doc_generator import DocumentationGenerator
from .notion_client import NotionClient
from .cli import NotionScribaCLI, main

__all__ = [
    "LLMProviderFactory",
    "BaseLLMProvider",
    "LLMConfig",
    "CodeAnalyzer",
    "DocumentationTemplates",
    "DocumentationGenerator",
    "NotionClient",
    "NotionScribaCLI",
    "main",
]
