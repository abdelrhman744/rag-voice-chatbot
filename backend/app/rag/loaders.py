import os
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_core.documents import Document

def load_documents(data_dir: str) -> list[Document]:
    docs: list[Document] = []
    if not os.path.exists(data_dir):
        return docs

    for fn in os.listdir(data_dir):
        path = os.path.join(data_dir, fn)

        if fn.lower().endswith(".pdf"):
            loaded = PyPDFLoader(path).load()
            # ضيف اسم الملف للمصدر بشكل واضح
            for d in loaded:
                d.metadata["file_name"] = fn
            docs.extend(loaded)

        elif fn.lower().endswith((".txt", ".md")):
            loaded = TextLoader(path, encoding="utf-8").load()
            for d in loaded:
                d.metadata["file_name"] = fn
            docs.extend(loaded)

    return docs
