from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.logging import setup_logging
from app.schemas import ChatRequest, ChatResponse, StatusResponse
from app.rag.qa import answer_question
from app.rag.ingest import reindex_all
from app.rag.config import LLM_MODEL, EMBED_MODEL

setup_logging()

app = FastAPI(title="RAG Chatbot (Ollama)")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", response_model=StatusResponse)
def health():
    return {"status": "ok", "detail": f"llm={LLM_MODEL}, embed={EMBED_MODEL}"}

@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    return answer_question(req.message, req.history)

@app.post("/reindex")
def reindex():
    return {"status": "reindexed", **reindex_all()}
