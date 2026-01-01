# prlyn (Prompt Linter)

[![PyPI version](https://img.shields.io/pypi/v/prlyn.svg)](https://pypi.org/project/prlyn/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**prlyn** is a professional-grade static analysis tool for LLM prompts. Beyond basic linting, it provides a comprehensive suite of linguistic, security, and model-specific metrics to ensure your prompts are robust, efficient, and safe for production.

---

## 🌟 Why prlyn?

Developing effective prompts is often trial-and-error. prlyn brings **Engineering Rigor** to Prompt Engineering by:
- **Quantifying Quality**: Move from "it feels slow" to "Actionable Ratio is 0.45".
- **Detecting Vulnerabilities**: Identify design-time security flaws before they become runtime liabilities.
- **Ensuring Model Fit**: Adjust scores based on whether you are targeting GPT-4, Claude, or legacy models.
- **Preventing Regression**: Track metrics over time as you iterate on complex system instructions.

---

## 🚀 Key Features

### 1. Design-time Security (Prompt Shield)
prlyn doesn't just detect attacks; it flags **vulnerability patterns** in your system prompts:
- **Delimiter Analysis**: Verifies strong separation between instructions and user data.
- **Defensive Anchors**: Checks for mandatory safety instructions and negative constraints.
- **Reflexive Leakage**: Identifies instructions that might inadvertently reveal your prompt's inner workings.

### 2. Advanced Linguistics
- **Flow Cohesion**: Uses semantic embeddings to detect "logical jumps" or disjointed instructions that confuse models.
- **Instructional Strength**: Quantifies the assertiveness of your commands using weighted verb analysis (e.g., *Must* vs. *Try*).
- **Position Scoring**: Detects the "lost middle" phenomenon by measuring instructional density at the context window's edges.

### 3. Model-Aware Intelligence
Use the `--model` flag to tailor analysis to specific LLM quirks:
- **GPT-4**: Penalizes "buried" instructions more heavily due to known recency bias.
- **Claude 3.5**: Adjusts thresholds for excellent long-context retrieval capabilities.

### 4. Prompt Shadowing (Iterative Development)
- **Automatic History**: Every scan is stored in a hidden `.prlyn/` directory.
- **Regression Detection**: Use `prlyn --diff` to compare your current draft against the previous version and see how your scores changed.

---

## 📦 Quick Start

Run **prlyn** directly without cloning or manual installation using `uvx`:

```bash
# Basic analysis
uvx --from git+https://github.com/mthangaraj/prlyn prlyn "Your prompt here..."

# Show all options
uvx --from git+https://github.com/mthangaraj/prlyn prlyn --help
```

---

## 🛠 Usage

### CLI Usage
```bash
# Basic analysis (if already running via uvx as shown above)
uvx --from git+https://github.com/mthangaraj/prlyn prlyn "Your prompt here..."
```

# Model-specific analysis
prlyn "..." --model gpt-4

# Compare current version to history
prlyn "..." --diff
---

### MCP Server (For AI Agents)
prlyn is a first-class **Model Context Protocol (MCP)** server. AI agents can use it to self-correct their own prompt generation.

#### 1. Claude Desktop
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "prlyn": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/mthangaraj/prlyn",
        "prlyn"
      ]
    }
  }
}
```

#### 2. Cursor
1. Go to **Settings** > **Cursor Settings** > **Features** > **MCP**.
2. Click **+ Add New MCP Server**.
3. Name: `prlyn`
4. Type: `command`
5. Command: `uvx --from git+https://github.com/mthangaraj/prlyn prlyn`

#### 3. Antigravity
Add the following to your MCP configuration:
```json
{
  "mcpServers": {
    "prlyn": {
      "command": "uvx",
      "args": [
        "--from", "git+https://github.com/mthangaraj/prlyn",
        "prlyn"
      ]
    }
  }
}
```

#### 4. Automated Rewriting
prlyn supports **self-correction workflows**. Your agent can:
1.  Call `prlyn.analyze_prompt(prompt)` to get a quality score.
2.  If the score is low, call `prlyn.get_improvement_template(prompt)`.
3.  Use the returned **Actionable Template** to rewrite its own prompt.

---

## 🔭 Technical Details

- **NLP Engine**: Spacy (`en_core_web_sm`) for linguistic structure and POS tagging.
- **Embeddings**: SentenceTransformers (`all-MiniLM-L6-v2`) for semantic similarity and flow analysis.
- **Tokenizer**: `tiktoken` for accurate token budget estimation.

---

## 💻 For Developers

If you want to contribute to **prlyn**:

```bash
# Clone the repository
git clone https://github.com/mthangaraj/prlyn.git
cd prlyn

# Install dependencies and setup environment
uv sync
```

Refer to [CONTRIBUTING.md](file:///Users/mthangaraj/my_projects/sage/prlyn/CONTRIBUTING.md) for more details.
