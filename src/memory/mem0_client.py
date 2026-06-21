from mem0 import MemoryClient
import os
import streamlit as st

MEM0_API_KEY = (
    st.secrets.get("MEM0_API_KEY")
    or os.getenv("MEM0_API_KEY")
)

memory = MemoryClient(
    api_key=MEM0_API_KEY
)