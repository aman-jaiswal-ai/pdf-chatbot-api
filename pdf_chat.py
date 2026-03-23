from fastapi import FastAPI, UploadFile, File
from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

app = FastAPI()

llm = ChatGroq(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="llama-3.3-70b-versatile"
)

vectorstore = None

@app.get("/")
def home():
    return {"message": "PDF Chatbot chal raha hai!"}

@app.post("/upload-pdf")
def upload_pdf(file: UploadFile = File(...)):
    global vectorstore

    with open("temp.pdf", "wb") as f:
        shutil.copyfileobj(file.file, f)

    loader = PyMuPDFLoader("temp.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectorstore = FAISS.from_documents(chunks, embeddings)

    return {"message": f"PDF upload ho gaya! {len(chunks)} chunks bane."}

@app.post("/ask")
def ask_question(question: str):
    if vectorstore is None:
        return {"error": "Pehle PDF upload karo!"}

    docs = vectorstore.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""Neeche diye gaye context ke basis pe sawaal ka jawab do.
    
Context:
{context}

Sawaal: {question}

Jawab:"""

    response = llm.invoke(prompt)
    return {"answer": response.content}