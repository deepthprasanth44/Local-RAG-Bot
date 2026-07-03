import sys
import subprocess

import streamlit as st

from rag import ask_question
from utils import (
    save_uploaded_file,
    get_uploaded_pdf
)

from config import (
    APP_TITLE,
    APP_DESCRIPTION,
    PAGE_ICON,
    LAYOUT,
    SUCCESS_UPLOAD,
    SUCCESS_VECTOR_DB,
    NO_DOCUMENT_MESSAGE
)

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)

# ---------------- Session State ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = None

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.title("🧠 Local AI Assistant")

    st.markdown("---")

    uploaded_file = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )

    current_pdf = get_uploaded_pdf()

    if current_pdf:
        st.success(f"📄 Current Document\n\n{current_pdf}")
    else:
        st.info("📄 No document uploaded")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.success("Chat cleared!")

# ---------------- Main Page ---------------- #

st.title(APP_TITLE)

st.caption(APP_DESCRIPTION)

st.info(
    """
### 👋 Welcome

Upload any PDF and ask questions about its contents.

### How to use

1. Upload a PDF.
2. Wait for the vector database to be created.
3. Ask questions.
4. View the answer and retrieved source context.
"""
)

st.divider()

# ---------------- Upload ---------------- #

if uploaded_file is not None:

    # Only process when a NEW file is uploaded
    if uploaded_file.name != st.session_state.uploaded_file_name:

        save_uploaded_file(uploaded_file)

        st.success(SUCCESS_UPLOAD)

        with st.spinner("Creating vector database..."):

            result = subprocess.run(
                [sys.executable, "ingest.py"],
                capture_output=True,
                text=True
            )

        if result.returncode == 0:

            st.success(SUCCESS_VECTOR_DB)

            st.session_state.uploaded_file_name = uploaded_file.name

            st.rerun()

        else:

            st.error("Failed to create vector database.")

            st.code(result.stderr)

# ---------------- Display Chat ---------------- #

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

# ---------------- Chat Input ---------------- #

question = st.chat_input(
    "Ask a question about the uploaded document..."
)

if question:

    current_pdf = get_uploaded_pdf()

    if current_pdf is None:

        st.warning(NO_DOCUMENT_MESSAGE)

        st.stop()

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer, docs = ask_question(question)

        st.write(answer)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.markdown("---")
        st.subheader("📚 Source Context")

        for i, doc in enumerate(docs, start=1):

            page = doc.metadata.get("page", "Unknown")

            with st.expander(f"📄 Source {i} • Page {page}"):

                st.write(doc.page_content)

# ---------------- Footer ---------------- #

st.markdown("---")

st.caption(
    "Built with Ollama • LangChain • ChromaDB • Streamlit"
)