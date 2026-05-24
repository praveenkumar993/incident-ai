# 🚨 Incident AI Ops Center

An end-to-end multi-agent AI incident intelligence platform built using CrewAI, FastAPI, React, Groq LLM, and LangSmith observability.

---

# 🔥 Overview

Incident AI Ops Center is an autonomous AI-powered incident analysis platform designed for modern production systems.

The platform analyzes infrastructure incidents, identifies root causes, suggests remediation actions, and generates structured incident intelligence reports using a multi-agent orchestration workflow.

The system also includes:
- real-time AI observability
- dynamic incident analytics
- interactive dashboard visualizations
- production-style AI workflows

---

# 🚀 Features

## 🤖 Multi-Agent AI Workflow
- Log Analysis Agent
- Root Cause Investigation Agent
- Remediation Planning Agent
- Final Report Generation Agent

## 📊 Interactive Dashboard
- Dynamic severity metrics
- Incident visualization charts
- Glassmorphism UI
- AI loading scanner animations
- Drag & drop JSON upload

## 🧠 AI Infrastructure
- CrewAI orchestration
- Groq LLM integration
- LangSmith tracing & observability
- FastAPI backend APIs

## 📈 Real-Time Incident Intelligence
- Root cause analysis
- Infrastructure impact analysis
- Severity assessment
- Remediation recommendations

---

# 🏗️ Architecture

```text
React Frontend
        ↓
FastAPI Backend
        ↓
CrewAI Multi-Agent System
        ↓
Groq LLM
        ↓
LangSmith Observability
```

---

# 🛠️ Tech Stack

## Frontend
- React
- Vite
- TailwindCSS
- Framer Motion
- Recharts
- React Hot Toast

## Backend
- FastAPI
- CrewAI
- LangChain
- Groq
- LangSmith
- Python

---

# 📂 Project Structure

```text
incident-ai/
│
├── agents/
├── configs/
├── crew/
├── frontend/
├── mcp_servers/
├── tools/
│
├── main.py
├── requirements.txt
├── render.yaml
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# ⚡ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/incident-ai-platform.git

cd incident-ai-platform
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup Environment Variables

Create `.env`

```env
GROQ_API_KEY=your_groq_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=incident-ai
```

---

# 🚀 Run Backend

```bash
uvicorn mcp_servers.log_server:app --reload
```

Backend:
```text
http://localhost:8000
```

---

# 🚀 Run Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:
```text
http://localhost:5173
```

---

# 📊 Sample Incident Logs

```json
{
  "incident_logs": [
    {
      "service": "payment-service",
      "severity": "critical",
      "message": "Primary PostgreSQL database unreachable"
    },
    {
      "service": "gateway-service",
      "severity": "high",
      "message": "CPU usage exceeded 95%"
    }
  ]
}
```

---

# 🔍 LangSmith Observability

The platform integrates with LangSmith for:
- agent execution tracing
- orchestration visibility
- token usage monitoring
- AI workflow debugging

---

# 🐳 Docker Support

Run locally with Docker:

```bash
docker compose up --build
```

---

# ☁️ Deployment

## Frontend
Deploy using:
- Vercel

## Backend
Deploy using:
- Render
- Railway

---

# 🚀 Future Improvements

- Prometheus integration
- Grafana monitoring
- Kubernetes metrics ingestion
- Real-time streaming incidents
- Authentication system
- Multi-tenant dashboards
- Vector database memory

---

# 👨‍💻 Author

Praveen Kumar

---

# ⭐ If You Like This Project

Give it a star on GitHub 🚀