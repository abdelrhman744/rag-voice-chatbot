import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

from app.rag.config import DATA_DIR, DB_DIR, EMBED_MODEL, CHUNK_SIZE, CHUNK_OVERLAP
from app.rag.loaders import load_documents

def reindex_all() -> dict:
    # 1) افتح نفس الـ persist_directory
    os.makedirs(DB_DIR, exist_ok=True)

    embeddings = OllamaEmbeddings(model=EMBED_MODEL)

    vs = Chroma(
        persist_directory=DB_DIR,
        embedding_function=embeddings,
    )

    # 2) امسح الـ collection الحالي (بدون لمس ملفات sqlite مباشرة)
    # Chroma default collection name is "langchain"
    try:
        vs._client.delete_collection("langchain")
    except Exception:
        # لو مش موجودة أو اسم مختلف، تجاهل
        pass

    # 3) حمّل الدوكيومنتس واعمل chunks
    docs = load_documents(DATA_DIR)
    if not docs:
        return {"indexed": 0, "chunks": 0, "note": "No documents found in /data"}

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(docs)

    # 4) ابني collection جديدة بنفس الـ persist directory
    vs2 = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=DB_DIR,
        collection_name="langchain",
    )

    return {"indexed": len(docs), "chunks": len(chunks)}
