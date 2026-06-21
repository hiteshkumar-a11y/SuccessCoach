from langchain_openai import ChatOpenAI
import streamlit as st

CHAT_MODEL = "gpt-5.4-mini-2026-03-17"

OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise Exception("OPENAI_API_KEY missing")

llm = ChatOpenAI(
    model=CHAT_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=0.3
)