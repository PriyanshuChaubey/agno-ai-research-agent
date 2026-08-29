# AI Research Agent

An AI-powered research agent built using **Agno** and **Groq**. The agent can understand user queries, use external tools for information retrieval, and generate concise, context-aware responses.

## 🚀 Features

* LLM-powered AI agent
* Built with the Agno agent framework
* Uses Qwen LLM through Groq
* Web search using DuckDuckGo
* Hacker News integration
* Tool-using agent workflow
* Markdown-formatted responses
* Automatic date and time context
* Environment-based API key management

## 🛠️ Tech Stack

* **Python**
* **Agno**
* **Groq**
* **Qwen**
* **DuckDuckGo**
* **Hacker News**
* **python-dotenv**

## 🧠 How It Works

The agent receives a user query and can use external tools when additional information is required.

```text
User Query
    ↓
Agno AI Agent
    ↓
Qwen LLM via Groq
    ↓
Tool Selection
    ├── DuckDuckGo Search
    └── Hacker News
    ↓
Process Retrieved Information
    ↓
Generate Final Response
```

## 📂 Project Structure

```text
ai-research-agent/
│
├── agent.py
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

> `.env` contains secret API credentials and is intentionally excluded from GitHub.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/PriyanshuChaubey/agno-ai-research-agent.git
cd agno-ai-research-agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Never commit your `.env` file or expose your API key publicly.

## ▶️ Run the Agent

```bash
python agent.py
```

The agent will process the configured query and use its available tools when required.

## 🔮 Future Improvements

* Add an interactive Streamlit interface
* Support user-provided queries
* Add conversation memory
* Add more external tools and APIs
* Implement structured responses
* Add agent evaluation and logging
* Deploy the agent as a web application

## 👨‍💻 Author

**Priyanshu Chaubey**

B.Tech – Artificial Intelligence & Robotics

Dayananda Sagar University

* LinkedIn: https://linkedin.com/in/priyanshu-chaubey
* GitHub: https://github.com/PriyanshuChaubey
* Portfolio: https://priyanshuchaubey.github.io
