from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

OPENAI_API_KEY = st.secrets.get(
    "OPENAI_API_KEY",
    os.getenv("OPENAI_API_KEY")
)

GOOGLE_SHEET_ID = st.secrets.get(
    "GOOGLE_SHEET_ID",
    os.getenv("GOOGLE_SHEET_ID")
)

MEM0_API_KEY = st.secrets.get(
    "MEM0_API_KEY",
    os.getenv("MEM0_API_KEY")
)