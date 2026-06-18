from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

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