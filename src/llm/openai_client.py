from langchain_openai import ChatOpenAI

from src.config.settings import (
    OPENAI_API_KEY,
    CHAT_MODEL
)

llm = ChatOpenAI(
    model=CHAT_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=0.3
)