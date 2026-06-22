import pandas as pd
import streamlit as st

from src.student_data.google_sheet_service import (
signal_sheet,
calendar_service
)

from src.planning.daily_planner import (
generate_daily_plan
)

from src.planning.scheduler import (
schedule_plan
)

from src.briefing.brief_generator import (
generate_student_brief
)

from src.meeting_notes.notes_ui import (
show_meeting_notes_form
)

def show_dashboard():
    st.title("🚨 Coach Dashboard")

    records = signal_sheet.get_all_records()

    if not records:
        st.success("No active student alerts")
        return

    df = pd.DataFrame(records)

    if df.empty:
        st.success("No active student alerts")
        return

    df["severity"] = (
        df["severity"]
        .astype(str)
        .str.upper()
    )

    df["urgency"] = (
        df["urgency"]
        .astype(str)
        .str.upper()
    )

    # --------------------------------
    # Metrics
    # --------------------------------

    critical_count = len(
        df[df["severity"] == "CRITICAL"]
    )

    high_count = len(
        df[df["severity"] == "HIGH"]
    )

    immediate_count = len(
        df[df["urgency"] == "IMMEDIATE"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🚨 Critical",
        critical_count
    )

    col2.metric(
        "⚠️ High",
        high_count
    )

    col3.metric(
        "⏰ Immediate",
        immediate_count
    )

    st.divider()

    # --------------------------------
    # Replanning Updates
    # --------------------------------

    if "plan_update_summary" in st.session_state:

        st.warning(
            f"""


    🔔 Plan Updated

    {st.session_state['plan_update_summary']}
    """
    )


    if "coach_decision" in st.session_state:

        decision = (
            st.session_state[
                "coach_decision"
            ]
        )

        st.error(
            "⚠️ Coach Decision Required"
        )

        st.write(
            decision["summary"]
        )

        col1, col2 = st.columns(2)

        with col1:

            st.button(
                f"Keep {decision['student_1']} Today"
            )

        with col2:

            st.button(
                f"Keep {decision['student_2']} Today"
            )

    # --------------------------------
    # Immediate Action
    # --------------------------------

    immediate = df[
        df["urgency"] == "IMMEDIATE"
    ]

    if len(immediate) > 0:

        st.subheader(
            "🚨 Immediate Action Required"
        )

        for _, row in immediate.iterrows():

            st.error(
                f"""


    **Student:** {row['student_id']}

    **Signal:** {row['signal_type']}

    {row.get('coach_summary', row.get('reason', 'No summary available'))}
    """
    )


    # --------------------------------
    # High Priority
    # --------------------------------

    high_priority = df[
        (df["severity"] == "HIGH")
        &
        (df["urgency"] != "IMMEDIATE")
    ]

    if len(high_priority) > 0:

        st.subheader(
            "⚠️ High Priority"
        )

        for _, row in high_priority.iterrows():

            st.warning(
                f"""


    **Student:** {row['student_id']}

    **Signal:** {row['signal_type']}

    {row.get('coach_summary', row.get('reason', 'No summary available'))}
    """
    )


    st.divider()

    # --------------------------------
    # Generate Plan
    # --------------------------------

    if st.button(
        "📅 Generate Today's Plan"
    ):

        if "plan_update_summary" in st.session_state:
            del st.session_state[
                "plan_update_summary"
            ]

        if "coach_decision" in st.session_state:
            del st.session_state[
                "coach_decision"
            ]

        plan = generate_daily_plan()

        plan = schedule_plan(
            plan,
            calendar_service
        )

        st.session_state[
            "daily_plan"
        ] = plan

    if "daily_plan" not in st.session_state:
        return

    plan = st.session_state[
        "daily_plan"
    ]

    # --------------------------------
    # Student Brief Section
    # --------------------------------

    st.divider()

    st.header(
        "📋 Student Brief"
    )

    all_students = []

    for student in plan["today"]:
        all_students.append(student)

    for student in plan["deferred"]:
        all_students.append(student)

    if len(all_students) > 0:

        student_map = {
            s["student_id"]: s
            for s in all_students
        }

        selected_student = st.selectbox(
            "Select Scheduled Student",
            list(student_map.keys())
        )

        if st.button(
            "Generate Brief"
        ):

            selected = student_map[
                selected_student
            ]

            st.info(
                f"""


    Meeting Information

    Student:
    {selected['student_id']}

    Session:
    {selected['session_type']}

    Time:
    {selected.get('time_slot', 'Tomorrow')}
    """
    )


            brief = generate_student_brief(
                selected_student
            )

            st.markdown(
                brief
            )

    # --------------------------------
    # Today's Schedule
    # --------------------------------

    st.divider()

    st.header(
        "📅 Today's Schedule"
    )

    if len(plan["today"]) == 0:

        st.info(
            "No students scheduled today"
        )

    else:

        for student in plan["today"]:

            with st.expander(
                f"{student['student_id']} | {student['time_slot']}"
            ):

                st.write(
                    f"Session: {student['session_type']}"
                )

                st.write(
                    f"Reason: {student['reason']}"
                )

                show_meeting_notes_form(
                    student["student_id"]
                )

    # --------------------------------
    # Deferred
    # --------------------------------

    if len(plan["deferred"]) > 0:

        st.header(
            "⏳ Deferred To Tomorrow"
        )

        for student in plan["deferred"]:

            st.info(
                f"""


    Student:
    {student['student_id']}

    Reason:
    {student['reason']}
    """
    )
