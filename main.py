# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Mera pehla API!", "status": "chal raha hai"}


# from fastapi import FastAPI
# from groq import Groq
# from dotenv import load_dotenv
# import os

# load_dotenv()

# app=FastAPI()
# client = Groq(api_key=os.getenv("OPENAI_API_KEY"))

# @app.get("/")
# def home():
#     return {"message": "AI API chal rahi hai!"}

# @app.post("/chat")
# def chat(message: str):
#     response = client.chat.completions.create(
#         model="llama-3.3-70b-versatile",
#         messages=[
#             {"role": "user", "content": message}
#         ]
#     )
#     return {"reply": response.choices[0].message.content}

# from fastapi import FastAPI
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, SystemMessage
# from dotenv import load_dotenv
# import os

# load_dotenv()

# app = FastAPI()

# llm = ChatGroq(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     model="llama-3.3-70b-versatile"
# )

# @app.get("/")
# def home():
#     return {"message": "LangChain AI API chal rahi hai!"}

# @app.post("/chat")
# def chat(message: str):
#     messages = [
#         SystemMessage(content="Tum ek expert Python teacher ho. Hamesha simple examples ke saath samjhao."),
#         HumanMessage(content=message)
#     ]
#     response = llm.invoke(messages)
#     return {"reply": response.content}


from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

llm = ChatGroq(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="llama-3.3-70b-versatile"
)

conversation_history = []

@app.get("/")
def home():
    return {"message": "Memory wali AI API chal rahi hai!"}

@app.post("/chat")
def chat(message: str):
    conversation_history.append(HumanMessage(content=message))

    messages = [
        SystemMessage(content="Tum ek helpful assistant ho jo Hinglish mein jawab deta hai.")
    ] + conversation_history

    response = llm.invoke(messages)

    conversation_history.append(AIMessage(content=response.content))

    return {
        "reply": response.content,
        "total_messages": len(conversation_history)
    }

@app.delete("/clear")
def clear():
    conversation_history.clear()
    return {"message": "Conversation clear ho gaya!"}