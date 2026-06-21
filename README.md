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

## 🏗️ Architecture

```
Agentic Healthcare Assistant
├── Agent Planning Layer
│   ├── Goal Decomposition
│   ├── Task Sequencing
│   └── Tool Selection
├── Execution Layer
│   ├── Tool Executor
│   ├── Memory Manager
│   └── Error Handler
├── Integration Layer
│   ├── Appointment API
│   ├── EHR Database
│   ├── Medical Search
│   └── Vector Store
└── Presentation Layer
    ├── Streamlit UI
    ├── Analytics Dashboard
    └── User Management
```

## 📋 Prerequisites

- Python 3.9+
- PostgreSQL 13+
- Redis 6+
- MongoDB 5+ (optional)
- OpenAI API Key
- Bing Search API Key

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/JusDh22/healthcare-assistant.git
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
# Edit .env with your API keys and configurations
```

### 5. Initialize Database
```bash
docker-compose up -d
python -c "from src.database.db_manager import init_db; init_db()"
```

### 6. Run Application
```bash
streamlit run ui/streamlit_app.py
```

## 📚 Usage Examples

### Example 1: Appointment Booking with Medical Context
```python
from src.agents.executor import AgentExecutor

executor = AgentExecutor()

query = """
My 70-year-old father has chronic kidney disease. 
I want to book a nephrologist for him. 
Also, can you summarize latest treatment methods?
"""

result = executor.execute_plan(
    user_query=query,
    session_id="session_123"
)
```

## 🔐 Security & Compliance

- ✅ HIPAA Compliance ready
- ✅ Data encryption at rest and in transit
- ✅ Patient data privacy controls
- ✅ Audit logging for all operations
- ✅ Role-based access control

## 📝 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💼 Author

**Project Lead**: Darshan Mangaldas Naik
