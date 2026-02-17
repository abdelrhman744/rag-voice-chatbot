from langchain_ollama import OllamaLLM
from app.rag.store import get_retriever
from app.rag.config import LLM_MODEL, TEMPERATURE

def answer_question(question: str, history: list) -> dict:
    retriever = get_retriever()
    docs = retriever.invoke(question)
    

    if not docs:
        return {
            "answer": "مش لاقي معلومات في ملفات /data تساعدني أجاوب. جرّب تضيف ملفات ثم اعمل /reindex.",
            "sources": []
        }

    context = "\n\n".join([f"- {d.page_content}" for d in docs])

    # history مختصر
    hist_text = ""
    for h in (history or [])[-6:]:
        role = (h.get("role") or "user").upper()
        content = h.get("content") or ""
        hist_text += f"{role}: {content}\n"

    prompt = f"""
You are a helpful assistant. Use ONLY the provided context to answer.
If the answer is not in the context, say you don't know and ask the user to provide the missing document.

CONTEXT:
{context}

CHAT HISTORY:
{hist_text}

QUESTION:
{question}

ANSWER:
""".strip()

    llm = OllamaLLM(model=LLM_MODEL, temperature=TEMPERATURE)
    answer = llm.invoke(prompt)

    sources = []
    for d in docs:
        sources.append({
            "file_name": d.metadata.get("file_name"),
            "source": d.metadata.get("source"),
            "page": d.metadata.get("page"),
        })

    return {"answer": answer, "sources": sources}
