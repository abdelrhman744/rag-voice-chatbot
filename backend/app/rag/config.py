from pathlib import Path

# file: backend/app/rag/config.py
# parents:
# 0 = rag
# 1 = app
# 2 = backend
# 3 = project root (rag-voice-chatbot)

BACKEND_DIR = Path(__file__).resolve().parents[2]
PROJECT_DIR = Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_DIR / "data"
DB_DIR   = BACKEND_DIR / "chroma_db"

LLM_MODEL = "llama3.2"              # خليه نفس اللي عندك في ollama list
EMBED_MODEL = "nomic-embed-text"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
TOP_K = 4
TEMPERATURE = 0.2

print("DATA_DIR =", DATA_DIR)
print("DB_DIR   =", DB_DIR)
