import streamlit as st

from src.meeting_notes.meeting_notes_service import (
    save_meeting_note
)


def show_meeting_notes_form(
    student_id
):

    st.subheader(
        f"Meeting Notes - {student_id}"
    )

    discussion = st.text_area(
        "Discussion Summary"
    )

    actions = st.text_area(
        "Action Items"
    )

    followup = st.date_input(
        "Follow-up Date"
    )

    risk = st.selectbox(
        "Risk Level",
        [
            "LOW",
            "MEDIUM",
            "HIGH"
        ]
    )

    if st.button(
        f"Save Notes {student_id}"
    ):

        save_meeting_note(
            student_id,
            discussion,
            actions,
            str(followup),
            risk
        )

        st.success(
            "Meeting notes saved"
        )