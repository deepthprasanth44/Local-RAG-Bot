"""
Application Configuration
-------------------------
This file contains all configurable settings used throughout the project.
"""

# ---------------- Folder Paths ---------------- #

DOCUMENT_FOLDER = "documents"
UPLOAD_FOLDER = "uploads"
CHROMA_DB = "chroma_db"

# ---------------- Ollama ---------------- #

OLLAMA_MODEL = "llama3.2:3b"

# ---------------- Embeddings ---------------- #

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# ---------------- Text Splitter ---------------- #

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# ---------------- Retriever ---------------- #

TOP_K_RESULTS = 3

# ---------------- Streamlit ---------------- #

APP_TITLE = "🧠 Local AI Document Assistant"

APP_DESCRIPTION = (
    "Ask questions about your uploaded PDF using "
    "Ollama + LangChain + ChromaDB"
)

PAGE_ICON = "🧠"

LAYOUT = "wide"

# ---------------- Messages ---------------- #

NO_DOCUMENT_MESSAGE = (
    "Please upload a PDF before asking questions."
)

NO_ANSWER_MESSAGE = (
    "I couldn't find that information in the uploaded document."
)

SUCCESS_UPLOAD = " PDF uploaded successfully!"

SUCCESS_VECTOR_DB = " Vector database created successfully!"