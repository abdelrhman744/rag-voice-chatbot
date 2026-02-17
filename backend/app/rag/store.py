import os
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from app.rag.config import DB_DIR, EMBED_MODEL, TOP_K

_vectorstore = None

def get_vectorstore():
    global _vectorstore
    if _vectorstore is None:
        os.makedirs(DB_DIR, exist_ok=True)
        embeddings = OllamaEmbeddings(model=EMBED_MODEL)
        _vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    return _vectorstore

def get_retriever():
    return get_vectorstore().as_retriever(search_kwargs={"k": TOP_K})
