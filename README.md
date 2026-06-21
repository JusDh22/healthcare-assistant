# 🏥 Agentic Healthcare Assistant

A comprehensive AI-powered healthcare assistant system that automates medical task management, appointment booking, medical record retrieval, and medical information search using advanced agentic AI frameworks.

## 🎯 Features

### Core Functionality
- **Agentic AI Planning**: Intelligent decomposition of complex medical queries into executable sub-tasks
- **Appointment Management**: Automated booking, tracking, and cancellation of medical appointments
- **Medical Records Management**: Structured storage and retrieval of patient medical history
- **Disease Information Search**: Integration with medical databases (Medline, WHO) for up-to-date health information
- **Patient Context Memory**: Long-term memory management for personalized interactions

### Advanced Components
- **RAG Pipeline**: Retrieval-Augmented Generation for accurate medical information
- **Vector Database (FAISS)**: Efficient similarity search for patient summaries
- **Memory Modules**: Persistent context management across sessions
- **Tool Logging**: Comprehensive monitoring of all tool executions
- **LLMOps Dashboard**: Real-time metrics and evaluation

## 📋 Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Redis 6+
- MongoDB 5+ (optional)
- OpenAI API Key
- Bing Search API Key

## 🚀 Quick Start

### 1. Create Project Directory
```bash
mkdir healthcare-assistant
cd healthcare-assistant
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment
```bash
cp .env.example .env
# Edit .env with your API keys
```

### 5. Start Services
```bash
docker-compose up -d
```

### 6. Initialize Database
```bash
python -c "from src.database.db_manager import init_db; init_db()"
```

### 7. Run Application
```bash
streamlit run ui/streamlit_app.py
```

## 📚 Project Structure

```
healthcare-assistant/
├── src/
│   ├── agents/          # Agent planning & execution
│   ├── tools/           # Tool implementations
│   ├── llm/             # LLM chains & prompts
│   ├── database/        # Database models & operations
│   └── utils/           # Configuration & logging
├── ui/
│   ├── streamlit_app.py # Main dashboard
│   └── pages/           # UI pages
├── tests/               # Test suite
├── docker-compose.yml   # Service orchestration
├── requirements.txt     # Python dependencies
└── .env.example         # Environment template
```

## 🔐 Security & Compliance

- ✅ HIPAA Compliance ready
- ✅ Data encryption at rest and in transit
- ✅ Patient data privacy controls
- ✅ Audit logging for all operations
- ✅ Role-based access control

## 📝 License

MIT License - see LICENSE file for details
