# RAG Voice Chatbot (Ollama)

A Retrieval-Augmented Generation chatbot using:

- FastAPI (Backend)
- Chroma (Vector DB)
- Ollama (LLM + Embeddings)
- Next.js (Frontend)
- Voice input (Speech-to-Text)

## Features
- Ask questions from local documents
- Arabic & English support
- Voice queries from browser
- Local LLM (no API keys required)

## Setup

### Backend
cd backend
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

### Frontend
cd frontend
npm install
npm run dev

## Data
Put your files inside `/data` and call `/reindex`.
