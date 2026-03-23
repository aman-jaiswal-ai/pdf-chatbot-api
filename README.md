# 📄 PDF Chatbot API

Upload any PDF and chat with it using AI!

## 🚀 What it does
1. User uploads any PDF
2. System reads and splits it into small chunks
3. Each chunk is converted into vectors (numbers)
4. When user asks a question — relevant chunks are found
5. AI gets those chunks + question
6. AI gives the answer

## 🛠️ Tech Stack
- **FastAPI** — Backend API
- **LangChain** — AI pipeline
- **FAISS** — Vector search
- **Groq LLM** — AI model (llama-3.3-70b)
- **Python** — Language

## ⚙️ Setup

1. Clone the repo
git clone https://github.com/aman-jaiswal-ai/pdf-chatbot-api.git
cd pdf-chatbot-api

2. Install dependencies
pip install -r requirements.txt

3. Create .env file
OPENAI_API_KEY=your_groq_api_key_here

4. Run the server
uvicorn main:app --reload

## 📬 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/upload` | Upload a PDF |
| POST | `/chat` | Ask a question |
| GET | `/` | Health check |
