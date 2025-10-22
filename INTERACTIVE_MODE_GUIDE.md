# 🏛️ Notion Scriba - Interactive Mode Guide

## Overview

The **Interactive Mode** provides an omnibox-style interface where you can type prompts and get intelligent file suggestions with TAB completion.

---

## 🚀 Quick Start

### Launch Interactive Mode

```bash
cd /path/to/your/project
scriba --interactive
# or
scriba -i
```

### What You'll See

```
======================================================================
🏛️  NOTION SCRIBA - Interactive Mode
   "Verba volant, scripta manent"
======================================================================

📂 Project: /your/project/path
📁 Files found: 127 Python files

💡 Tips:
   • Start typing to see file suggestions
   • Press TAB to autocomplete file names
   • Type multiple files separated by commas
   • Press Ctrl+D or type 'exit' to quit
======================================================================

scriba> █
```

---

## 💡 Usage Examples

### 1. **Mention Files in Your Prompt**

Just type naturally and include file names:

```
scriba> Explain what postgres_agent.py does
```

The system will automatically:
- ✅ Detect `postgres_agent.py` in your prompt
- ✅ Locate the file in your project
- ✅ Show file metadata (LOC, size)
- ✅ Ask for confirmation before generating docs

### 2. **Use TAB Completion**

Start typing and press TAB:

```
scriba> Analyze post█
         ↓ [TAB]
         ↓
scriba> Analyze postgres_agent.py
```

The autocomplete will show:
- Matching files
- Line count (LOC)
- File size

### 3. **Multiple Files**

Mention multiple files in one prompt:

```
scriba> Explain how postgres_agent.py interacts with langgraph_engine.py
```

Both files will be detected:
```
✅ Files detected: 2
   1. core/postgres_agent.py (420 LOC)
   2. core/langgraph/langgraph_engine.py (580 LOC)
```

### 4. **Natural Language**

Just type naturally:

```
scriba> What does the authentication system in auth.py do?
scriba> Document the API endpoints in api_routes.py
scriba> Explain the database schema in models.py
```

---

## 🎯 File Detection

### How It Works

The interactive mode:
1. **Scans** your project directory for Python files (`.py`)
2. **Excludes** common directories (`__pycache__`, `.git`, `venv`, etc.)
3. **Indexes** file names and paths
4. **Parses** your prompt for file references
5. **Suggests** completions as you type

### Supported File Extensions

By default:
- ✅ `.py` (Python files)

Future support planned:
- �� `.js`, `.ts` (JavaScript/TypeScript)
- 🔜 `.go` (Go)
- 🔜 `.rs` (Rust)
- 🔜 `.java` (Java)

---

## ⌨️ Keyboard Shortcuts

| Key | Action |
|-----|--------|
| **TAB** | Autocomplete file name |
| **↑** | Previous command (history) |
| **↓** | Next command (history) |
| **Ctrl+D** | Exit interactive mode |
| **Ctrl+C** | Cancel current input |

---

## 🎨 Features

### ✅ Implemented

- 🔍 **Intelligent File Scanner**: Automatically finds all Python files
- 📝 **TAB Completion**: Autocomplete file names as you type
- 🎯 **File Detection**: Parses file references from natural language
- 📊 **Metadata Display**: Shows LOC and file size
- 🎨 **Beautiful UI**: Latin-themed prompt with styled output
- 📚 **Command History**: Navigate previous prompts with arrow keys
- 🚀 **Multi-file Support**: Detect multiple files in one prompt

### 🔜 Coming Soon

- 🤖 **Live Documentation Generation**: Generate docs directly from interactive mode
- 🔗 **Notion Integration**: Sync to Notion with confirmation
- 🎛️ **Template Selection**: Choose doc template interactively
- 🌐 **Multi-language Support**: Support for JS, TS, Go, Rust, etc.
- 💾 **Session Persistence**: Save and resume interactive sessions

---

## 🛠️ Advanced Usage

### Custom Project Root

```bash
scriba --interactive --project-root /path/to/project
```

### Combined with Other Flags

```bash
# Use specific LLM provider
scriba -i --provider anthropic

# Set custom template
scriba -i --template technical-deep-dive

# Debug mode
scriba -i --debug
```

---

## 🐛 Troubleshooting

### "No files detected"

**Problem**: Your prompt doesn't mention any file names

**Solution**: 
- Include actual file names from your project
- Use TAB completion to see available files
- Type partial file names and press TAB

### "Files found: 0"

**Problem**: No Python files in current directory

**Solution**:
- Navigate to your project directory first
- Or specify `--project-root /path/to/project`

### Autocomplete not working

**Problem**: TAB doesn't show suggestions

**Solution**:
- Make sure you've typed at least 2 characters
- Check that `prompt-toolkit` is installed: `pip list | grep prompt`
- Verify you're in a project with `.py` files

---

## 💡 Tips & Tricks

### 1. **Start Generic, Get Specific**

```
scriba> auth█  [TAB]
# Shows: auth.py, auth_handler.py, authentication.py
```

### 2. **Use Relative Paths**

If you see duplicates, use relative paths:

```
scriba> core/auth.py
```

### 3. **Combine with Natural Language**

```
scriba> Explain the purpose and main functions of database_manager.py
```

### 4. **Review Before Generating**

The system always shows detected files and asks for confirmation:
```
✅ Files detected: 1
   1. src/auth.py (245 LOC)

📝 Generate documentation for these files? [Y/n]:
```

---

## 🎯 Use Cases

### 1. **Exploring Unknown Codebases**

```
scriba> What does main.py do?
scriba> Explain the entry point in app.py
```

### 2. **Documenting Specific Components**

```
scriba> Document the authentication flow in auth_service.py
```

### 3. **Understanding Integrations**

```
scriba> How does api_client.py interact with database.py?
```

### 4. **Quick File Discovery**

```
scriba> [Type partial name] + TAB
```

---

## 📚 Example Session

```bash
$ cd /workspaces/myproject
$ scriba -i

======================================================================
🏛️  NOTION SCRIBA - Interactive Mode
   "Verba volant, scripta manent"
======================================================================

📂 Project: /workspaces/myproject
📁 Files found: 47 Python files

scriba> What does auth█
        ↓ [TAB]
        auth.py
        auth_handler.py
        authentication.py

scriba> What does auth.py do?

✅ Files detected: 1
   1. src/auth.py (245 LOC)

📝 Generate documentation for these files? [Y/n]: y

🔍 Analyzing files...
🤖 Generating documentation with GPT-4o...
📤 Syncing to Notion...

✅ Done! Documentation created in Notion.

scriba> exit

👋 Exiting interactive mode...
```

---

## 🏛️ Philosophy

> **"Verba volant, scripta manent"** - Spoken words fly away, written words remain.

Interactive mode embodies this principle by making documentation generation as natural as conversation, while ensuring the output is permanent, structured, and valuable.

---

**Built with 🏛️ classical elegance and 🤖 modern intelligence**

*Notion Scriba - Where ancient wisdom meets artificial intelligence*
