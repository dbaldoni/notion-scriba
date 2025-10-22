"""
Notion Docs Synapse - AI-powered documentation generator for Notion.

A modular system for automatic bilingual documentation generation with support
for multiple LLM providers and direct Notion synchronization.
"""

__version__ = "1.0.0"

# Core components
from .llm import LLMProviderFactory, BaseLLMProvider, LLMConfig
from .code_analyzer import CodeAnalyzer
from .templates import DocumentationTemplates
from .doc_generator import DocumentationGenerator
from .notion_client import NotionClient
from .cli import NotionDocsCLI, main

__all__ = [
    "LLMProviderFactory",
    "BaseLLMProvider",
    "LLMConfig",
    "CodeAnalyzer",
    "DocumentationTemplates",
    "DocumentationGenerator",
    "NotionClient",
    "NotionDocsCLI",
    "main",
]

__version__ = "1.0.0"
__author__ = "Notion Docs Synapse Contributors"
__license__ = "MIT"

from .llm import BaseLLMProvider, LLMConfig, LLMProviderFactory
from .code_analyzer import CodeAnalyzer
from .templates import DocumentationTemplates
from .doc_generator import DocumentationGenerator
from .notion_client import NotionClient

__all__ = [
    "BaseLLMProvider",
    "LLMConfig",
    "LLMProviderFactory",
    "CodeAnalyzer",
    "DocumentationTemplates",
    "DocumentationGenerator",
    "NotionClient",
    "__version__",
]
