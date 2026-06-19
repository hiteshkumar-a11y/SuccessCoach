import streamlit as st
from src.chatbot.assistant import get_answer

st.set_page_config(
    page_title="Student Success Coach",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Student Success Coach")
st.caption("Ask questions about your attendance, marks, exams, and academic performance.")

# Sidebar
st.sidebar.header("Student Details")

student_id = st.sidebar.text_input(
    "Student ID",
    placeholder="e.g. Stu1"
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask your question..."):

    if not student_id:
        st.error("Please enter Student ID in the sidebar.")
        st.stop()

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = get_answer(
    prompt,
    student_id,
    st.session_state.messages
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