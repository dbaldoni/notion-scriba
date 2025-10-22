#!/usr/bin/env python3
"""
Example usage script for Notion Scriba.

Demonstrates how to use the library programmatically.
"""

import os
from dotenv import load_dotenv

from notion_scriba import (
    LLMProviderFactory,
    LLMConfig,
    CodeAnalyzer,
    DocumentationGenerator,
    NotionClient
)

def main():
    """Run example workflow."""
    
    # Load environment
    load_dotenv()
    
    print("\n" + "="*60)
    print("🏛️  NOTION SCRIBA - EXAMPLE WORKFLOW")
    print("="*60 + "\n")
    
    # Step 1: Initialize LLM provider
    print("1️⃣  Initializing LLM provider...")
    
    provider_name = os.getenv("LLM_PROVIDER", "openai")
    api_key = os.getenv("OPENAI_API_KEY")  # or ANTHROPIC_API_KEY, etc.
    
    if not api_key and provider_name != "ollama":
        print(f"❌ No API key found for {provider_name}")
        print("   Set API key in .env or run: scriba-setup")
        return
    
    config = LLMConfig(
        api_key=api_key or "",
        model="gpt-4o",  # or any supported model
        temperature=0.3,
        max_tokens=4000
    )
    
    llm_provider = LLMProviderFactory.create(provider_name, config)
    print(f"   ✅ {provider_name.upper()} provider ready")
    
    # Step 2: Analyze code (optional)
    print("\n2️⃣  Analyzing code...")
    
    analyzer = CodeAnalyzer()
    
    # Example: analyze current project
    analysis = analyzer.analyze_directory(
        "src/notion_docs_synapse",
        max_files=10
    )
    
    if analysis:
        print(f"   ✅ Analyzed {analysis.get('total_files', 0)} files")
        print(f"      Total LOC: {analysis.get('total_lines', 0)}")
    else:
        print("   ⚠️  No analysis (directory not found)")
        analysis = None
    
    # Step 3: Generate documentation
    print("\n3️⃣  Generating documentation...")
    
    doc_gen = DocumentationGenerator(llm_provider)
    
    try:
        it_doc, en_doc = doc_gen.generate_bilingual(
            component="notion_docs_synapse",
            template_name="technical-deep-dive",
            user_prompt="Generate comprehensive technical documentation for this project",
            code_analysis=analysis
        )
        
        print(f"   ✅ Documentation generated!")
        print(f"      IT: {len(it_doc)} characters")
        print(f"      EN: {len(en_doc)} characters")
        
    except Exception as e:
        print(f"   ❌ Generation failed: {e}")
        return
    
    # Step 4: Sync to Notion (if configured)
    print("\n4️⃣  Syncing to Notion...")
    
    notion_token = os.getenv("NOTION_TOKEN")
    
    if not notion_token:
        print("   ⚠️  Notion not configured (skipping)")
        print("      Run: scriba-setup")
    else:
        client = NotionClient(
            token=notion_token,
            db_it=os.getenv("NOTION_DB_IT"),
            db_en=os.getenv("NOTION_DB_EN"),
            page_it=os.getenv("NOTION_PAGE_IT"),
            page_en=os.getenv("NOTION_PAGE_EN")
        )
        
        # Test connection
        success, message = client.test_connection()
        if not success:
            print(f"   ❌ Connection failed: {message}")
            return
        
        print(f"   ✅ Connected ({client.mode} mode)")
        
        # Sync IT
        print("      🇮🇹 Syncing Italian...")
        it_success = client.update_page(
            title="Notion Scriba",
            content=it_doc,
            lang="it",
            create_backup=True,
            merge_mode=False
        )
        
        # Sync EN
        print("      🇬🇧 Syncing English...")
        en_success = client.update_page(
            title="Notion Scriba",
            content=en_doc,
            lang="en",
            create_backup=True,
            merge_mode=False
        )
        
        if it_success and en_success:
            print("   ✅ Sync complete!")
        else:
            print("   ⚠️  Partial sync (check logs)")
    
    # Success
    print("\n" + "="*60)
    print("🎉 WORKFLOW COMPLETE!")
    print("="*60 + "\n")
    
    print("💡 Try the CLI for easier usage:")
    print("   scriba --component myapp --template technical-deep-dive")
    print("   scriba --provider anthropic --quick 'Generate docs'")
    print("   scriba --list-providers")
    print()


if __name__ == "__main__":
    main()
