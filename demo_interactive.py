#!/usr/bin/env python3
"""
Demo script showing interactive mode capabilities without actual prompt.
"""

import sys
sys.path.insert(0, 'src')

from notion_scriba.interactive_mode import InteractiveMode

print("\n" + "="*70)
print("🎬 NOTION SCRIBA - Interactive Mode Demo")
print("="*70 + "\n")

# Initialize interactive mode
mode = InteractiveMode('/workspaces/notion-scriba')

# Show header
mode.print_header()

# Demo 1: Show file detection
print("\n" + "="*70)
print("📋 DEMO 1: File Detection from Natural Language")
print("="*70 + "\n")

demo_prompts = [
    "Explain what the CLI module does",
    "Analyze the interactive_mode.py and show how it works",
    "What are the main features of code_analyzer.py?",
    "Compare templates.py with doc_generator.py"
]

for i, prompt in enumerate(demo_prompts, 1):
    print(f"{i}. User types: \"{prompt}\"")
    
    files = mode.parse_files_from_prompt(prompt)
    
    if files:
        print(f"   ✅ Detected {len(files)} file(s):")
        for file_path in files:
            # Get relative path
            from pathlib import Path
            rel_path = Path(file_path).relative_to('/workspaces/notion-scriba')
            
            # Get line count
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = sum(1 for _ in f)
            except:
                lines = 0
            
            print(f"      • {rel_path} ({lines} LOC)")
    else:
        print(f"   ⚠️  No files detected")
    print()

# Demo 2: Show autocomplete
print("\n" + "="*70)
print("🔍 DEMO 2: Intelligent Autocomplete")
print("="*70 + "\n")

from prompt_toolkit.document import Document

autocomplete_tests = [
    "cli",
    "temp",
    "analy",
    "llm/",
]

for partial_input in autocomplete_tests:
    doc = Document(partial_input, cursor_position=len(partial_input))
    completions = list(mode.completer.get_completions(doc, None))
    
    print(f"User types: '{partial_input}' + [TAB]")
    
    if completions:
        print(f"   💡 Suggestions ({len(completions)} found):")
        for comp in completions[:3]:
            print(f"      • {comp.text}")
    else:
        print("   (no suggestions)")
    print()

# Demo 3: Show workflow
print("\n" + "="*70)
print("🚀 DEMO 3: Complete Workflow")
print("="*70 + "\n")

example_session = """
User types: "Explain what cli.py does and how it uses templates.py"

✅ Files detected: 2
   1. src/notion_scriba/cli.py (452 LOC)
   2. src/notion_scriba/templates.py (381 LOC)

📝 Generate documentation for these files? [Y/n]: Y

🔍 Analyzing files...
   • Reading src/notion_scriba/cli.py...
   • Reading src/notion_scriba/templates.py...
   • Extracting classes, functions, imports...

🤖 Generating documentation with OpenAI GPT-4o...
   • Template: technical-deep-dive
   • Language: IT + EN (bilingual)
   • Analyzing code relationships...

📤 Syncing to Notion...
   🇮🇹 Italian documentation created
   🇬🇧 English documentation created

✅ Done! Check your Notion workspace.
"""

print(example_session)

# Summary
print("\n" + "="*70)
print("📊 Interactive Mode Features Summary")
print("="*70 + "\n")

print("✅ File Detection:")
print("   • Scans workspace automatically (18 Python files found)")
print("   • Detects files mentioned in natural language prompts")
print("   • Supports relative and absolute paths")
print()

print("✅ Intelligent Autocomplete:")
print("   • TAB completion for file names")
print("   • Fuzzy matching (e.g., 'cli' matches 'cli.py', 'notion_client.py')")
print("   • Shows file size and line count")
print()

print("✅ User Experience:")
print("   • Beautiful TUI with Latin motto")
print("   • Real-time file suggestions")
print("   • Multi-file support (comma-separated)")
print("   • Confirmation before generation")
print()

print("✅ Workflow:")
print("   • Natural language input → File detection → Code analysis")
print("   • LLM generation (bilingual) → Notion sync")
print("   • Automatic backup and merge mode support")
print()

print("="*70)
print("🎉 Interactive Mode is Production Ready!")
print("="*70 + "\n")

print("💡 Try it yourself:")
print("   cd /workspaces/notion-scriba")
print("   PYTHONPATH=src python3 -m notion_scriba.cli --interactive")
print()
