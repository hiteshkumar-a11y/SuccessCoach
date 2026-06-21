from dotenv import load_dotenv
import os


import streamlit as st

load_dotenv()
OPENAI_API_KEY = (
    st.secrets.get("OPENAI_API_KEY")
    or os.getenv("OPENAI_API_KEY")
)

GOOGLE_SHEET_ID = (
    st.secrets.get("GOOGLE_SHEET_ID")
    or os.getenv("GOOGLE_SHEET_ID")
)

MEM0_API_KEY = (
    st.secrets.get("MEM0_API_KEY")
    or os.getenv("MEM0_API_KEY")
)

CHAT_MODEL = os.getenv(
    "CHAT_MODEL",
    "gpt-5.4-mini-2026-03-17"
)

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "text-embedding-3-small"
)

CHROMA_PATH = os.getenv(
    "CHROMA_PATH",
    "chroma_db"
)

COLLECTION_NAME = os.getenv(
    "COLLECTION_NAME",
    "student_kb"
)