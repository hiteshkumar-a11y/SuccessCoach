import streamlit as st

print("SECRETS KEYS:", list(st.secrets.keys()))

OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")

print("OPENAI FOUND:", OPENAI_API_KEY is not None)
print("OPENAI LENGTH:", len(OPENAI_API_KEY) if OPENAI_API_KEY else 0)