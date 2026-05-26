# 🚨 Incident AI Ops Center

An enterprise-grade multi-agent AI incident intelligence platform built using CrewAI, FastAPI, React, Groq LLM, LangSmith observability, and Vector Memory Search.

---

# 🔥 Overview

Incident AI Ops Center is an autonomous AI-powered incident analysis and operational intelligence platform designed for modern production environments.

The platform ingests infrastructure incidents from multiple formats, performs AI-driven root cause analysis using multi-agent orchestration, generates remediation strategies, and retrieves semantically similar historical incidents using vector memory.

The system combines:
- AI agents
- observability workflows
- semantic incident memory
- vector similarity search
- production-style incident intelligence
- real-time interactive dashboards

---

# 🚀 Core Features

## 🤖 Multi-Agent AI Workflow

The platform uses a CrewAI-powered autonomous agent system:

- Log Analysis Agent
- Root Cause Investigation Agent
- Remediation Planning Agent
- Final Report Generation Agent

---

# 🧠 AI Operational Intelligence

## ✅ Vector Database Memory
- Persistent historical incident storage
- Semantic incident embeddings
- Historical outage retrieval
- Similarity-based operational intelligence

## ✅ Semantic Similarity Search

The platform retrieves historically related incidents using vector similarity search powered by embeddings and ChromaDB.

---

# 🏗️ System Architecture

## High-Level Architecture

```text
                         ┌──────────────────────┐
                         │  User Uploads Logs   │
                         │ JSON / CSV / LOG/TXT │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌────────────────────────────┐
                    │   Frontend React Dashboard │
                    │  Tailwind + Framer Motion  │
                    └──────────┬─────────────────┘
                               │ API Calls
                               ▼
                   ┌─────────────────────────────┐
                   │     FastAPI Backend         │
                   │ Incident Processing Engine  │
                   └──────────┬──────────────────┘
                              │
          ┌───────────────────┼────────────────────┐
          │                   │                    │
          ▼                   ▼                    ▼

┌────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│ Normalization  │  │ Vector Memory DB │  │ CrewAI Agents    │
│ Layer          │  │ ChromaDB         │  │ Multi-Agent Flow │
└────────────────┘  └──────────────────┘  └──────────────────┘
                              │                    │
                              ▼                    ▼

                  ┌────────────────────┐  ┌──────────────────┐
                  │ Similarity Search  │  │ Groq LLM         │
                  │ Historical Memory  │  │ AI Reasoning     │
                  └────────────────────┘  └──────────────────┘
                               │
                               ▼
                   ┌────────────────────────────┐
                   │ AI Incident Intelligence   │
                   │ Report Generation          │
                   └──────────┬─────────────────┘
                              │
                              ▼
                   ┌────────────────────────────┐
                   │ LangSmith Observability    │
                   │ Agent Tracing & Monitoring │
                   └────────────────────────────┘
```

---

# ⚡ Tech Stack

## Frontend
- React
- Vite
- TailwindCSS
- Framer Motion
- Recharts
- React Hot Toast
- Lucide Icons
- React Dropzone

## Backend
- FastAPI
- CrewAI
- LangChain
- Groq LLM
- LangSmith
- ChromaDB
- Sentence Transformers
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
├── memory/
├── parsers/
├── mcp_servers/
├── vector_db/
├── tools/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── render.yaml
├── vercel.json
├── README.md
└── .env
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/incident-ai.git

cd incident-ai
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Install Frontend Packages

```bash
cd frontend

npm install
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=incident-ai
```

---

# 🚀 Running Backend

```bash
uvicorn mcp_servers.log_server:app --reload
```

---

# 🚀 Running Frontend

```bash
cd frontend

npm run dev
```

---

# 🐳 Docker Support

```bash
docker compose up --build
```

---

# ☁️ Deployment

## Frontend
- Vercel

## Backend
- Render
- Railway

---

# 👨‍💻 Author

Praveen Kumar

---

# ⭐ Support

If you like this project, give it a star on GitHub 🚀
