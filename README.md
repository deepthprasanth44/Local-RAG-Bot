# 🧠 Local AI Document Assistant

A local Retrieval-Augmented Generation (RAG) chatbot that answers questions from uploaded PDF documents using **Ollama**, **LangChain**, **ChromaDB**, and **Streamlit**.

The application runs completely on your local machine without requiring any cloud-based LLM services.

---

# Features

-  Upload PDF documents
-  Ask questions about the uploaded document
-  Retrieves relevant document sections using ChromaDB
-  Generates answers using Ollama (llama3.2:3b)
-  Displays the retrieved source context
-  Chat-style interface
-  Runs completely offline
-  Automatically updates the vector database when a new PDF is uploaded

---

# Technologies Used

- Python
- Ollama
- LangChain
- ChromaDB
- HuggingFace Embeddings
- Streamlit
- PyPDF
- Sentence Transformers

---

# Project Structure

```
Local-RAG-Bot/
│
├── app.py
├── ingest.py
├── rag.py
├── utils.py
├── config.py
├── test.py
├── requirements.txt
├── README.md
│
├── documents/
├── uploads/
└── chroma_db/
```

---

# How It Works

1. Upload a PDF document.
2. The document is read using PyPDFLoader.
3. The document is split into smaller chunks.
4. Each chunk is converted into embeddings using HuggingFace Embeddings.
5. The embeddings are stored in ChromaDB.
6. When a question is asked:
   - Relevant chunks are retrieved.
   - The retrieved context is sent to the Ollama LLM.
   - The model generates an answer based only on the uploaded document.

---

# Installation

## Clone the Repository

```bash
git clone <repository-url>
cd Local-RAG-Bot
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com

---

## Download the Model

```bash
ollama pull llama3.2:3b
```

---

# Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your default web browser.

---

# Sample Questions

Example questions you can ask:

- What is an API?
- Explain REST API.
- What are the different types of APIs?
- Summarize this document.
- What is SOAP?
- What are the advantages of APIs?
- What is the conclusion of the document?

---

# Example Workflow

```
Upload PDF
      │
      ▼
Read PDF
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
      │
      ▼
Ask Question
      │
      ▼
Retrieve Relevant Chunks
      │
      ▼
Generate Answer using Ollama
      │
      ▼
Display Answer + Source Context
```

---

# Future Improvements

- Support multiple PDF documents
- Support DOCX and TXT files
- Conversation memory
- Citation with page numbers
- Model selection from the UI
- Dark mode support
- Export chat history
- Voice input support

---

# Advantages

- Runs completely offline
- No API key required
- Fast document retrieval
- Privacy-focused
- Easy to use
- Modular architecture

---

# Requirements

- Python 3.11 or later
- Ollama
- llama3.2:3b model
- Streamlit
- LangChain
- ChromaDB

---

# Author

Deepth Prasanth

B.Tech Computer Science Engineering

AI/ML Enthusiast

---

# License

This project is developed for educational purposes and internship evaluation.
