# 📄 PDF Chatbot API

GenAI-powered PDF chatbot built using FastAPI, LangChain, FAISS, HuggingFace embeddings, and Groq LLM for intelligent document querying.

---

# 🚀 Features

- Upload and process PDF documents
- AI-powered question answering
- Semantic search using vector embeddings
- FastAPI backend with REST APIs
- Context-aware responses using RAG architecture
- Swagger API documentation support

---

# 🧠 How It Works

1. User uploads a PDF document
2. PDF content is extracted and split into chunks
3. Text chunks are converted into vector embeddings
4. FAISS performs semantic similarity search
5. Relevant context is passed to the LLM
6. AI generates intelligent answers

---

# 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **LangChain**
- **FAISS**
- **HuggingFace Embeddings**
- **Groq LLM (Llama 3.3 70B)**

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/aman-jaiswal-ai/pdf-chatbot-api.git
cd pdf-chatbot-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the server:

```bash
uvicorn main:app --reload
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload PDF |
| POST | `/chat` | Ask questions |
| GET | `/` | Health check |

---

# 📌 Future Improvements

- Multi-PDF support
- Chat history memory
- Authentication system
- Streamlit frontend
- Cloud deployment

---

# 👨‍💻 Author

Aman Jaiswal

- LinkedIn:  
https://www.linkedin.com/in/amanjaiswal-aiml/

- GitHub:  
https://github.com/aman-jaiswal-ai
