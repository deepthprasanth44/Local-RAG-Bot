import os
import shutil

from config import (
    DOCUMENT_FOLDER,
    CHROMA_DB,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def load_documents():
    """
    Load all PDF documents from the documents folder.
    """

    documents = []

    if not os.path.exists(DOCUMENT_FOLDER):
        raise FileNotFoundError(
            f"'{DOCUMENT_FOLDER}' folder not found."
        )

    pdf_files = [
        file
        for file in os.listdir(DOCUMENT_FOLDER)
        if file.lower().endswith(".pdf")
    ]

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files found in the documents folder."
        )

    for file in pdf_files:

        path = os.path.join(DOCUMENT_FOLDER, file)

        if os.path.getsize(path) == 0:
            print(f"Skipping empty file: {file}")
            continue

        print(f"Reading: {file}")

        loader = PyPDFLoader(path)

        documents.extend(loader.load())

    return documents


def split_documents(documents):
    """
    Split documents into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)


def create_embeddings():
    """
    Load HuggingFace embedding model.
    """

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )


def build_vector_database(chunks, embedding):
    """
    Create a fresh Chroma vector database.
    """

    if os.path.exists(CHROMA_DB):
        shutil.rmtree(CHROMA_DB)

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory=CHROMA_DB,
    )

    return db


def main():

    print("=" * 60)
    print("Creating Vector Database")
    print("=" * 60)

    try:

        documents = load_documents()

        print(f"Loaded {len(documents)} pages.")

        chunks = split_documents(documents)

        print(f"Created {len(chunks)} chunks.")

        embedding = create_embeddings()

        build_vector_database(chunks, embedding)

        print()
        print("Vector database created successfully!")
        print("=" * 60)

    except Exception as e:

        print()
        print("Error while creating vector database")
        print(e)
        print("=" * 60)


if __name__ == "__main__":
    main()