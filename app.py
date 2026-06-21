import streamlit as st
from src.chatbot.assistant import get_answer
from src.signals.signal_detector import detect_signal
from src.student_data.google_sheet_service import add_signal
from src.coach.dashboard import show_dashboard

st.set_page_config(
    page_title="Student Success Coach",
    page_icon="🎓",
    layout="wide"
)
page = st.sidebar.radio(
    "View",
    [
        "Student Chat",
        "Coach Dashboard"
    ]
)
if page == "Coach Dashboard":

    show_dashboard()

    st.stop()

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
if st.button("End Session"):


    conversation = ""

    for msg in st.session_state.messages:

        conversation += (
            f"{msg['role']}: "
            f"{msg['content']}\n"
        )

    signal = detect_signal(
        conversation
    )

    if signal.get(
        "signal_detected",
        False
    ):

        add_signal(
            student_id=student_id,
            signal_type=signal["signal_type"],
            severity=signal["severity"],
            urgency=signal["urgency"],
            reason=signal["reason"]
        )

    st.session_state.messages = []

    st.rerun()



