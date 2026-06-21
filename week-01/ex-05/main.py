import os, logging
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Dict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Easy-ChatGPT Proxy Baseline")

@app.on_event("startup")
async def startup_event():
    logging.getLogger("uvicorn.info").info("La aplicación está lista en http://127.0.0.1:6661/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(base_url=os.getenv("OPENAI_ENDPOINT"), api_key=os.getenv("OPENAI_API_KEY"))
MODEL_NAME = os.getenv("MODEL")

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]

@app.get("/")
async def read_index():
    return FileResponse("index.html")

@app.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        response = client.chat.completions.create(model=MODEL_NAME, messages=request.messages, temperature=0.7)
        answer = response.choices[0].message.content
        usage = response.usage
        return {"answer": answer, "usage": {"prompt_tokens": usage.prompt_tokens, "completion_tokens": usage.completion_tokens, "total_tokens": usage.total_tokens}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
