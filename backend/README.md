# Backend - RAG Chatbot (Ollama)

## 1) Prerequisites
- Ollama installed
- Models:
  - llama3.2
  - nomic-embed-text

## 2) Install
Activate venv then:
pip install -r requirements.txt

## 3) Run API
uvicorn app.main:app --reload --port 8000

## 4) Put your files
Put PDFs/TXT/MD into: ../data/

## 5) Reindex
Open:
http://127.0.0.1:8000/docs
Then call POST /reindex
