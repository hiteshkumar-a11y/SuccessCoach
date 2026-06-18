# app.py

import streamlit as st
from src.chatbot.rag_pipeline import get_answer

st.set_page_config(
    page_title="Student Success Coach",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Ask your query")
st.caption("Ask questions about your academic performance")

# Sidebar
student_id = st.sidebar.text_input(
    "Student ID",
    placeholder="Enter Student ID"
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask a question..."):

    # Validate student id
    if not student_id:
        st.error("Please enter Student ID in sidebar.")
        st.stop()

    # Show user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate answer
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = get_answer(
                    prompt,
                    student_id
                )

                st.markdown(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                error_message = f"Error: {str(e)}"

                st.error(error_message)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message
                    }
                )