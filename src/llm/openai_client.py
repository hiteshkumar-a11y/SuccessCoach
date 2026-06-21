from langchain_openai import ChatOpenAI

import os
import streamlit as st

from src.config.settings import (
    CHAT_MODEL
)

OPENAI_API_KEY = (
    st.secrets.get("OPENAI_API_KEY")
    or os.getenv("OPENAI_API_KEY")
)

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found in Streamlit Secrets or environment variables"
    )

llm = ChatOpenAI(
    model=CHAT_MODEL,
    api_key=OPENAI_API_KEY,
    temperature=0.3
)