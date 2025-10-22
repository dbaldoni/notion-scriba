# 🔧 Notion Setup Guide

Complete guide for configuring Notion integration with Notion Docs Synapse.

---

## 🚀 Quick Setup (Interactive Wizard)

The easiest way to configure Notion integration:

```bash
notion-docs setup
```

This interactive wizard will guide you through:
1. ✅ Creating/entering your Notion integration token
2. ✅ Choosing between Pages or Database mode
3. ✅ Entering the appropriate IDs
4. ✅ Validating the connection
5. ✅ Saving configuration to `.env`

---

## 📋 Manual Setup

### Step 1: Create Notion Integration

1. **Go to Integrations Page**
   - Visit: [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations)
   - Click **"New integration"**

2. **Configure Integration**
   - **Name**: Choose a descriptive name (e.g., "Docs Generator")
   - **Associated workspace**: Select your workspace
   - **Capabilities**: Ensure these are checked:
     - ✅ Read content
     - ✅ Update content
     - ✅ Insert content

3. **Copy Integration Token**
   - After creating, copy the **"Internal Integration Token"**
   - Format: `secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - ⚠️ Keep this secret! Don't commit to Git.

---

### Step 2: Choose Output Mode

#### Option A: Database Mode (Recommended) 🗄️

**Best for:**
- Multiple components
- Organized documentation
- Filtering and sorting
- Properties and views

**Setup:**

1. **Create Database(s)**
   - In Notion, create a new page
   - Type `/database` and select "Database - Full page"
   - Give it a title (e.g., "Documentation IT" and "Documentation EN")
   - Or use a single database for both languages

2. **Share Database with Integration**
   - Open the database
   - Click **"Share"** (top right)
   - Click **"Invite"**
   - Search for your integration name
   - Click **"Invite"**

3. **Get Database ID**
   - With database open, click **"Share"** → **"Copy link"**
   - URL format: `https://notion.so/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx?v=...`
   - The ID is the 32-character string (the `xxxx...` part)
   - Example: `2906d85c-ec32-80d3-a930-d3e0be89dd69`

4. **Add to `.env`**
   ```bash
   NOTION_TOKEN=secret_your-token-here
   
   # Single database (recommended)
   NOTION_DB_IT=your-database-id-here
   NOTION_DB_EN=your-database-id-here  # Same ID for bilingual
   
   # OR separate databases
   NOTION_DB_IT=your-italian-database-id
   NOTION_DB_EN=your-english-database-id
   ```

---

#### Option B: Pages Mode (Simple) 📄

**Best for:**
- Single component
- Simple setup
- Direct page updates

**Setup:**

1. **Create Pages**
   - Create two Notion pages:
     - One for Italian documentation
     - One for English documentation
   - Give them descriptive names

2. **Share Pages with Integration**
   - Open each page
   - Click **"Share"** (top right)
   - Click **"Invite"**
   - Search for your integration name
   - Click **"Invite"**
   - Repeat for both pages

3. **Get Page IDs**
   - With page open, click **"Share"** → **"Copy link"**
   - URL format: `https://notion.so/Page-Title-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx?v=...`
   - The ID is the 32-character string after the page title
   - Example: `2236d85c-ec32-80d9-8831-ec4f51d13ba0`

4. **Add to `.env`**
   ```bash
   NOTION_TOKEN=secret_your-token-here
   NOTION_PAGE_IT=your-italian-page-id
   NOTION_PAGE_EN=your-english-page-id
   ```

---

## 🔍 Finding Notion IDs

### Visual Guide

**Database/Page ID in URL:**
```
https://www.notion.so/workspace/Database-Name-2906d85cec3280d3a930d3e0be89dd69?v=...
                                          └─────────────┬─────────────┘
                                                   DATABASE ID (32 chars)
```

**Alternative Method (Inspector):**
1. Right-click page/database → **"Copy link"**
2. Paste in text editor
3. Extract the 32-character hex string
4. Format with dashes: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

---

## ✅ Testing Your Configuration

### Method 1: Via Wizard
```bash
notion-docs setup
# Wizard will validate connection automatically
```

### Method 2: Manual Test
```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("NOTION_TOKEN")
headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28"
}

response = requests.get(
    "https://api.notion.com/v1/users/me",
    headers=headers
)

if response.status_code == 200:
    print("✅ Connection successful!")
    print(f"Connected as: {response.json()['name']}")
else:
    print(f"❌ Connection failed: {response.status_code}")
```

### Method 3: Test Run
```bash
notion-docs --component test --template technical-deep-dive
```

---

## 🔒 Security Best Practices

1. **Never commit `.env` file**
   - Already in `.gitignore`
   - Use `.env.example` for documentation

2. **Rotate tokens if exposed**
   - Go to: https://www.notion.so/my-integrations
   - Click your integration → **"Secrets"** → **"Regenerate"**

3. **Limit integration permissions**
   - Only grant necessary capabilities
   - Share only required pages/databases

4. **Use environment-specific tokens**
   - Different tokens for dev/staging/production
   - Never share production tokens

---

## ❓ Troubleshooting

### ❌ "Invalid token" error

**Causes:**
- Token not copied correctly (missing `secret_` prefix)
- Token expired or regenerated
- Wrong workspace

**Solution:**
1. Verify token in `.env` starts with `secret_`
2. Check integration exists: https://www.notion.so/my-integrations
3. Regenerate token if needed

---

### ❌ "Page/Database not found" error

**Causes:**
- Integration not shared with page/database
- Wrong ID copied
- ID format incorrect

**Solution:**
1. Open page/database in Notion
2. Click **Share** → Verify integration is invited
3. Re-copy the link and extract ID correctly
4. Ensure ID is 32 characters (no URL parameters)

---

### ❌ "Insufficient permissions" error

**Causes:**
- Integration doesn't have required capabilities
- Parent page restrictions

**Solution:**
1. Go to integration settings
2. Enable: Read content, Update content, Insert content
3. Check parent page permissions

---

### ❌ Connection timeout

**Causes:**
- Network issues
- Notion API temporarily unavailable
- Firewall blocking requests

**Solution:**
1. Check internet connection
2. Verify Notion status: https://status.notion.so
3. Check corporate firewall/proxy settings

---

## 📚 Database Schema Recommendations

### Recommended Properties

For optimal organization, add these properties to your Notion database:

| Property | Type | Purpose |
|----------|------|---------|
| **Title** | Title | Component name |
| **Language** | Select | IT / EN |
| **Template** | Select | investment-grade, technical-deep-dive, etc. |
| **Status** | Select | Draft, Review, Published |
| **Last Updated** | Date | Auto-update timestamp |
| **Component** | Text | Source component path |
| **Version** | Text | Documentation version |

### Example Views

**Italian Docs:**
- Filter: Language = IT
- Sort: Last Updated (descending)

**English Docs:**
- Filter: Language = EN
- Sort: Last Updated (descending)

**By Template:**
- Group by: Template
- Sort: Last Updated

---

## 🎯 Next Steps

After setup, you can:

1. **Generate first documentation:**
   ```bash
   notion-docs --component myproject --template technical-deep-dive
   ```

2. **Configure LLM provider:**
   - Add API key to `.env`
   - See main README.md for provider setup

3. **Explore templates:**
   ```bash
   notion-docs --help
   ```

4. **Customize workflow:**
   - Use `--merge-mode` to preserve existing content
   - Use `--auto-code-analysis` for automatic code inspection
   - Use `--quick` for direct prompts

---

## 📧 Support

- 🐛 Found a bug? [Open an issue](https://github.com/yourusername/notion-docs-synapse/issues)
- 💬 Questions? [Start a discussion](https://github.com/yourusername/notion-docs-synapse/discussions)
- 📖 More docs: [README.md](../README.md)

---

<p align="center">
  Made with ❤️ by the Notion Docs Synapse community
</p>
