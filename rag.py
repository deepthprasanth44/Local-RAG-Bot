from config import (
    CHROMA_DB,
    EMBEDDING_MODEL,
    OLLAMA_MODEL,
    TOP_K_RESULTS,
)

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama


# ---------------- Embedding Model ---------------- #

embedding = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

# ---------------- Ollama Model ---------------- #

llm = ChatOllama(
    model=OLLAMA_MODEL
)


def get_retriever():
    """
    Load the Chroma database only when needed.
    This prevents Windows from locking chroma.sqlite3.
    """

    db = Chroma(
        persist_directory=CHROMA_DB,
        embedding_function=embedding
    )

    return db.as_retriever(
        search_kwargs={"k": TOP_K_RESULTS}
    )


def build_prompt(context, question):
    """
    Build the prompt for the language model.
    """

    return f"""
You are a helpful AI Document Assistant.

Answer ONLY using the information provided in the context.

Rules:

1. Never make up information.

2. If the answer cannot be found, reply exactly:

"I couldn't find that information in the uploaded document."

3. Keep answers short and professional.

4. Use bullet points whenever appropriate.

5. Do not mention the words "context" or "document chunks".

----------------------------------------------------

Context:

{context}

----------------------------------------------------

Question:

{question}

----------------------------------------------------

Answer:
"""


def ask_question(question):
    """
    Retrieve the most relevant chunks and generate an answer.
    """

    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    prompt = build_prompt(
        context,
        question
    )

    response = llm.invoke(prompt)

    return response.content, docs