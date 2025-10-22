# Contributing to Notion Scriba

Thank you for your interest in contributing to Notion Scriba.

Notion Scriba is released under the GNU General Public License v3 (GPLv3).
By contributing code, documentation, or other material to this project you
agree that your contributions will be licensed under the GPLv3.

How to contribute
1. Fork the repository and create a branch for your feature or fix.
2. Write tests where applicable and keep changes small and focused.
3. Open a pull request describing the change, referencing any issues.
4. Maintain the same license headers and include attribution if necessary.

Please ensure your contributions comply with the GPLv3 terms. If you
cannot license your contribution under GPLv3, please contact the
maintainers before submitting.

Code of Conduct
Please follow the community Code of Conduct available in `CODE_OF_CONDUCT.md`.
# Contributing to Notion Scriba

🏛️ **"Verba volant, scripta manent"** - Spoken words fly away, written words remain.

Thank you for your interest in contributing to Notion Scriba! This document explains how to contribute while respecting the project's GPL v3 license.

---

## 📋 Table of Contents

1. [License Agreement](#license-agreement)
2. [How to Contribute](#how-to-contribute)
3. [Development Setup](#development-setup)
4. [Code Standards](#code-standards)
5. [Pull Request Process](#pull-request-process)
6. [Commercial Use](#commercial-use)

---

## 🔐 License Agreement

Notion Scriba is licensed under the **GNU General Public License v3.0 (GPL v3)**.

### What This Means for Contributors

When you contribute code to this project, you agree that:

1. ✅ **Your contribution will be licensed under GPL v3**
2. ✅ **You retain copyright** of your contribution
3. ✅ **You grant everyone the right** to use, modify, and distribute your code under GPL v3 terms
4. ✅ **You confirm** you have the right to contribute the code (it's your original work or compatible with GPL v3)

### What This Means for Users

If you fork or modify Notion Scriba:

- ✅ **Personal use**: Use it freely, no obligation to share
- ✅ **Internal company use**: Use it freely, no obligation to share
- ⚠️ **Distribution**: If you distribute modified versions, you **MUST**:
  - Share the source code
  - License it under GPL v3
  - Include copyright notices
  - Document your changes
- ⚠️ **Commercial products**: If you sell software based on Notion Scriba, you **MUST** release the source code under GPL v3

**TL;DR**: You're free to use and modify, but if you distribute or sell modified versions, you must share the source code. No proprietary forks allowed.

---

## 🚀 How to Contribute

We welcome contributions! Here's how:

### 1. **Report Bugs** 🐛

Found a bug? [Open an issue](https://github.com/dbaldoni/notion-scriba/issues/new) with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment (OS, Python version, LLM provider)

### 2. **Suggest Features** 💡

Have an idea? [Open an issue](https://github.com/dbaldoni/notion-scriba/issues/new) with:
- Clear description of the feature
- Use case and benefits
- Proposed implementation (optional)

### 3. **Submit Code** 💻

Ready to code? Follow these steps:

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/notion-scriba.git
cd notion-scriba

# 3. Create a feature branch
git checkout -b feature/your-feature-name

# 4. Make your changes
# (see Development Setup below)

# 5. Test your changes
python -m pytest tests/

# 6. Commit with descriptive message
git commit -m "feat: add support for Gemini 2.0 provider"

# 7. Push to your fork
git push origin feature/your-feature-name

# 8. Open a Pull Request on GitHub
```

---

## 🛠️ Development Setup

### Prerequisites

- Python 3.10 or higher
- Git
- API keys for LLM providers (OpenAI, Anthropic, etc.)

### Setup Environment

```bash
# Clone the repository
git clone https://github.com/dbaldoni/notion-scriba.git
cd notion-scriba

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Copy environment template
cp .env.example .env
# Edit .env with your API keys

# Run setup wizard
scriba-setup

# Test installation
scriba --version
scriba -i  # Test interactive mode
```

### Project Structure

```
notion-scriba/
├── src/notion_scriba/     # Main package
│   ├── cli.py            # Command-line interface
│   ├── interactive_mode.py  # Interactive omnibox mode
│   ├── code_analyzer.py  # Python code analysis
│   ├── doc_generator.py  # Documentation generation
│   ├── notion_client.py  # Notion API integration
│   ├── setup_wizard.py   # Interactive configuration
│   ├── templates.py      # Documentation templates
│   └── llm/             # LLM provider implementations
│       ├── base.py      # Abstract base class
│       ├── factory.py   # Provider factory
│       ├── openai_provider.py
│       ├── anthropic_provider.py
│       ├── google_provider.py
│       ├── deepseek_provider.py
│       └── ollama_provider.py
├── tests/               # Test suite (to be added)
├── docs/               # Documentation
├── examples/           # Usage examples
└── pyproject.toml     # Package configuration
```

---

## 📐 Code Standards

### Style Guide

- **PEP 8**: Follow Python style guidelines
- **Type hints**: Use type annotations where appropriate
- **Docstrings**: Document all public functions and classes
- **Comments**: Explain complex logic

### Example

```python
def generate_documentation(
    code: str,
    template: str,
    language: str = "en"
) -> str:
    """
    Generate documentation from code using specified template.
    
    Args:
        code: Source code to document
        template: Documentation template name
        language: Output language (en or it)
    
    Returns:
        Generated documentation as string
    
    Raises:
        ValueError: If template is invalid
    """
    # Implementation...
```

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add support for Gemini 2.0 provider
fix: resolve Notion API rate limiting issue
docs: update setup wizard guide
refactor: simplify LLM provider factory
test: add unit tests for code analyzer
chore: update dependencies
```

---

## ✅ Pull Request Process

1. **Update Documentation**: If you change functionality, update README/docs
2. **Add Tests**: Include tests for new features (when test suite is available)
3. **Check Style**: Ensure code follows PEP 8
4. **Update CHANGELOG**: Add entry to CHANGELOG.md
5. **Sign Commits**: Use `git commit -s` to sign your commits
6. **Pass CI**: All checks must pass (when CI is set up)

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How did you test your changes?

## GPL v3 Compliance
- [ ] I confirm my contribution is compatible with GPL v3
- [ ] I have added GPL headers to new files
- [ ] I have documented any external dependencies and their licenses
```

---

## 💼 Commercial Use

### You CAN:

✅ Use Notion Scriba in your company  
✅ Modify it for internal use  
✅ Sell consulting services based on Notion Scriba  
✅ Integrate it into your workflow  

### You MUST (if distributing):

⚠️ **Release your modifications under GPL v3**  
⚠️ **Provide source code to users**  
⚠️ **Include copyright and license notices**  
⚠️ **Document your changes**  

### You CANNOT:

❌ Create proprietary closed-source versions  
❌ Remove or modify license headers  
❌ Distribute without providing source code  
❌ Claim ownership of the original work  

---

## 🤝 Code of Conduct

### Our Standards

- **Be respectful** - Treat everyone with respect
- **Be constructive** - Provide helpful feedback
- **Be collaborative** - Work together towards common goals
- **Be patient** - Remember we're all learning

### Unacceptable Behavior

- Harassment, discrimination, or personal attacks
- Trolling, insulting comments, or off-topic discussions
- Publishing others' private information
- Any conduct harmful to the project or community

### Enforcement

Violations may result in:
1. Warning
2. Temporary ban from the project
3. Permanent ban from the project

Report issues to: [create an issue](https://github.com/dbaldoni/notion-scriba/issues)

---

## 🎯 Priority Areas

We especially welcome contributions in these areas:

1. **LLM Providers**
   - Add support for new providers (Mistral, Cohere, etc.)
   - Improve error handling and rate limiting

2. **Templates**
   - Create new documentation templates
   - Support for more programming languages

3. **Testing**
   - Add unit tests
   - Add integration tests
   - Setup CI/CD pipeline

4. **Documentation**
   - Improve guides and tutorials
   - Add video demonstrations
   - Translate documentation to other languages

5. **Features**
   - Improve code analysis for other languages (JavaScript, TypeScript, Java, etc.)
   - Add support for more Notion features (databases, relations, etc.)
   - Improve interactive mode UX

---

## 📚 Resources

- **GPL v3 Full Text**: [LICENSE](./LICENSE)
- **GPL v3 FAQ**: https://www.gnu.org/licenses/gpl-faq.html
- **Project README**: [README.md](./README.md)
- **GitHub Issues**: https://github.com/dbaldoni/notion-scriba/issues

---

## 🙏 Thank You!

Every contribution helps make Notion Scriba better. Whether it's code, documentation, bug reports, or feedback - it all matters!

**Built with 🏛️ classical elegance and 🤖 modern intelligence**

*Notion Scriba - Where ancient wisdom meets artificial intelligence*

---

**License**: This project is licensed under GPL v3. See [LICENSE](./LICENSE) for details.
