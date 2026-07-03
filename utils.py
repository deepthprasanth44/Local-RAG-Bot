import os
import shutil

from config import (
    DOCUMENT_FOLDER,
    UPLOAD_FOLDER,
    CHROMA_DB,
)


def ensure_folders():
    """Create required folders if they don't exist."""

    os.makedirs(DOCUMENT_FOLDER, exist_ok=True)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def clear_documents():
    """Delete all PDFs from the documents folder."""

    if os.path.exists(DOCUMENT_FOLDER):

        for file in os.listdir(DOCUMENT_FOLDER):

            file_path = os.path.join(DOCUMENT_FOLDER, file)

            if os.path.isfile(file_path):
                os.remove(file_path)


def clear_uploads():
    """Delete all uploaded files."""

    if os.path.exists(UPLOAD_FOLDER):

        for file in os.listdir(UPLOAD_FOLDER):

            file_path = os.path.join(UPLOAD_FOLDER, file)

            if os.path.isfile(file_path):
                os.remove(file_path)


def clear_chroma_db():
    """Delete the Chroma vector database."""

    if os.path.exists(CHROMA_DB):

        shutil.rmtree(CHROMA_DB)


def save_uploaded_file(uploaded_file):
    """Save the uploaded PDF."""

    ensure_folders()

    clear_documents()

    file_path = os.path.join(
        DOCUMENT_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as file:

        file.write(uploaded_file.getbuffer())

    return file_path


def get_uploaded_pdf():
    """Return the current uploaded PDF."""

    ensure_folders()

    pdf_files = [
        file
        for file in os.listdir(DOCUMENT_FOLDER)
        if file.lower().endswith(".pdf")
    ]

    if pdf_files:
        return pdf_files[0]

    return None


def get_pdf_count():
    """Return number of uploaded PDFs."""

    ensure_folders()

    return len(
        [
            file
            for file in os.listdir(DOCUMENT_FOLDER)
            if file.lower().endswith(".pdf")
        ]
    )


def file_exists(filename):
    """Check if a file exists."""

    return os.path.exists(
        os.path.join(
            DOCUMENT_FOLDER,
            filename
        )
    )


def reset_application():
    """
    Reset the entire application.
    """

    clear_documents()

    clear_uploads()

    clear_chroma_db()

    ensure_folders()