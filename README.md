# AI Agents Collection

A collection of practical AI agent implementations built with **Agno**, **Groq**, and modern LLM-based tools. This repository contains different agent experiments demonstrating tool calling, web research, financial analysis, multi-agent workflows, and persistent conversation history.

The goal of this repository is to explore how LLMs can move beyond simple text generation and perform useful tasks by interacting with external tools, maintaining context, and coordinating between specialized agents.

---

## 🤖 Agents Included

### 1. Research Agent

A tool-using AI research agent capable of retrieving information from external sources.

**Capabilities:**

* Web search using DuckDuckGo
* Hacker News research
* LLM-powered reasoning and response generation
* Markdown-formatted responses
* Date and time context

**Technologies:**

* Python
* Agno
* Groq
* Qwen
* DuckDuckGo
* Hacker News

---

### 2. Finance Research Agent

An AI agent designed for financial and investment-related research using real-time financial data and external information sources.

**Capabilities:**

* Stock price lookup
* Historical stock performance analysis
* Financial data retrieval
* Web research
* Hacker News research
* Investment-oriented analysis
* Financial metrics and insights

**Tools:**

* YFinance
* DuckDuckGo
* Hacker News

**Technologies:**

* Python
* Agno
* Groq
* Qwen
* YFinance

The agent can combine financial data with external research to provide more comprehensive responses.

---

### 3. Multi-Agent System

A multi-agent implementation exploring how multiple specialized AI agents can work together to solve a task.

Instead of relying on a single general-purpose agent, the system demonstrates the concept of dividing responsibilities among specialized agents and coordinating their outputs.

**Concepts explored:**

* Multiple specialized agents
* Agent coordination
* Task delegation
* LLM-powered workflows
* Tool-based reasoning
* Combining outputs from multiple agents

---

### 4. Agent with Persistent Memory

An AI agent demonstrating persistent conversation history using **Agno + SQLite**.

The agent stores its session data in an SQLite database and adds previous conversation history to the model's context. This allows the agent to understand follow-up questions based on earlier interactions. Agno supports this pattern through `SqliteDb` and `add_history_to_context=True`.

**Example conversation:**

```text
User: What is the capital of Australia?
Agent: Canberra.

User: What is the best time to visit it?
Agent: ...
```

The second question can be interpreted using the context from the previous conversation.

**Technologies:**

* Python
* Agno
* Groq
* Qwen
* SQLite
* python-dotenv

---

## 🧠 Concepts Demonstrated

This repository explores several important concepts in modern AI application development:

* LLM integration
* AI Agents
* Agentic workflows
* Tool calling
* Web search
* Financial data retrieval
* Multi-agent systems
* Conversation history
* Persistent agent storage
* Prompt/instruction design
* Context management
* External API/tool integration
* Environment variable management

---

## 🛠️ Tech Stack

| Category               | Technologies  |
| ---------------------- | ------------- |
| Language               | Python        |
| Agent Framework        | Agno          |
| LLM Provider           | Groq          |
| LLM                    | Qwen          |
| Web Search             | DuckDuckGo    |
| News                   | Hacker News   |
| Financial Data         | YFinance      |
| Database               | SQLite        |
| Environment Management | python-dotenv |
| Version Control        | Git / GitHub  |

---

## 📁 Repository Structure

```text
ai-agents-collection/
│
├── research-agent/
│   └── agent.py
│
├── finance-agent/
│   └── agent.py
│
├── multi-agent/
│   └── agent.py
│
├── memory-agent/
│   └── memory.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

> The exact filenames and folder names may vary as the collection grows.

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/PriyanshuChaubey/agno-ai-research-agent.git
cd agno-ai-research-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never commit the `.env` file to GitHub.

---

## ▶️ Running an Agent

Navigate to the desired agent directory and run its Python file.

For example:

```bash
python agent.py
```

or:

```bash
python memory.py
```

---

## 🔐 Environment & Security

API credentials are loaded from environment variables using `python-dotenv`.

The `.env` file is intentionally excluded from version control.

Example `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
.vscode/
```

---

## 🚀 Future Improvements

* Add interactive Streamlit interfaces
* Add persistent user-specific memory
* Build more advanced multi-agent workflows
* Add additional external tools and APIs
* Add agent evaluation and test cases
* Add structured outputs
* Add logging and observability
* Deploy selected agents as web applications
* Improve error handling and tool reliability

---

## 👨‍💻 Author

**Priyanshu Chaubey**

B.Tech – Artificial Intelligence & Robotics
Dayananda Sagar University

* LinkedIn: https://www.linkedin.com/in/priyanshu-chaubey-03007b286/
* GitHub: https://github.com/PriyanshuChaubey
* Portfolio: https://priyanshuchaubey.github.io
