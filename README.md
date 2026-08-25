# 🤖 AI DevOps Pipeline Doctor (Autonomous CI/CD Failure Debugger Agent)

An event-driven, autonomous AI Agent built with LangGraph, Ollama (Llama 3.2), and GitHub Actions that detects pipeline failures, extracts build/test logs, analyzes root causes, submits automated code fix Pull Requests, and dispatches incident summary alerts to Discord.

---

## 🚀 Architectural Workflow

Workflow Trigger: GitHub Actions CI Failure
↓
Node 1: Fetch Failed Logs via GitHub API
↓
Node 2: Root Cause Analysis via Ollama (Llama 3.2)
↓
Node 3: Generate Code Fix & Patch Diffs
↓
Node 4: Create Auto-Fix Branch & Submit Pull Request
↓
Node 5: Send Rich Embed Notification to Discord Webhook

---

## ✨ Key Features

- Event-Driven Automation: Triggers dynamically on pipeline execution failures via GitHub Actions workflow_run.
- 100% Zero-Cost Architecture: Runs local LLM inference via Ollama (Llama 3.2) on GitHub-hosted runners — zero API keys or cloud costs required.
- Stateful Agent Workflow: Leverages LangGraph to handle a multi-node execution DAG (Fetch Logs -> Analyze -> Patch -> Git PR -> Notify).
- Autonomous Self-Healing: Generates clean code fixes, handles Git ref/branch creation, updates source code, and creates GitHub Pull Requests automatically via REST API.
- Instant Alerting: Formats diagnostic findings and outputs direct PR references to Discord Webhooks.

---

## 🛠️ Tech Stack

- Language: Python 3.10
- Agent Orchestration: LangGraph, LangChain
- LLM Engine: Ollama (Llama 3.2 Model)
- CI/CD Automation: GitHub Actions
- Integrations: GitHub REST API v3, Discord Webhook API
- Testing Framework: Pytest

---

## 📁 Repository Structure

.
├── .github/
│   └── workflows/
│       ├── ci.yml              # Primary CI workflow running pytest suite
│       └── agent-trigger.yml   # Event listener triggering AI Doctor on CI failure
├── agent/
│   ├── main.py                 # LangGraph Agent logic with all 5 nodes
│   └── requirements-agent.txt  # Python dependencies for the Agent
├── app.py                      # Core application code
├── test_app.py                 # Test suite containing mock assertion rules
└── requirements.txt            # Application dependencies

---

## ⚙️ Configuration & Secrets Setup

To run this agent in your repository, configure the following settings:

1. Repository Secrets
Navigate to Settings -> Secrets and variables -> Actions and add:
- DISCORD_WEBHOOK_URL: Your Discord channel webhook endpoint URL.

2. Actions Permissions
Navigate to Settings -> Actions -> General -> Workflow permissions:
- Select "Read and write permissions".
- Check "Allow GitHub Actions to create and approve pull requests".

---

## 💻 Local Setup & Testing

1. Clone the Repository:
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-devops-pipeline-doctor.git
cd ai-devops-pipeline-doctor

2. Setup Virtual Environment:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r agent/requirements-agent.txt

3. Run Ollama Locally:
ollama pull llama3.2

4. Test Agent Manually:
export GITHUB_TOKEN="your_personal_access_token"
export REPO_NAME="YOUR_USERNAME/ai-devops-pipeline-doctor"
export FAILED_RUN_ID="123456789"
export DISCORD_WEBHOOK_URL="your_discord_webhook_url"
python agent/main.py

---

## 🤝 Contributing & License

This project is built for educational and resume demonstration purposes showcasing Agentic AI in DevOps Pipelines. Feel free to fork and extend it with additional nodes like Slack notifications or Docker log parsing!
