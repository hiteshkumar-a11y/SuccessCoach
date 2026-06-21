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
     



    # ---------------------------
    # Normalize
    # ---------------------------

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

    # ---------------------------
    # Metrics
    # ---------------------------

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

    # ---------------------------
    # Immediate Action
    # ---------------------------

    immediate = df[
        df["urgency"] == "IMMEDIATE"
    ]

    if len(immediate) > 0:

        st.subheader("🚨 Immediate Action Required")

        for _, row in immediate.iterrows():

            st.error(
                f"""
**Student:** {row['student_id']}

**Signal:** {row['signal_type']}

{row.get('coach_summary', row.get('reason', 'No summary available'))}
"""
            )

    # ---------------------------
    # High Priority
    # ---------------------------

    high_priority = df[
        (df["severity"] == "HIGH")
        &
        (df["urgency"] != "IMMEDIATE")
    ]

    if len(high_priority) > 0:

        st.subheader("⚠️ High Priority")

        for _, row in high_priority.iterrows():

            st.warning(
                f"""
**Student:** {row['student_id']}

**Signal:** {row['signal_type']}

{row.get('coach_summary', row.get('reason', 'No summary available'))}
"""
            )

    st.divider()

    st.header("📋 Student Brief")
    students = sorted(
        df["student_id"].unique()
    )
    selected_student = st.selectbox(
        "Select Student",
        students
    )
    if st.button("Generate Brief"):

        brief = generate_student_brief(
            selected_student
        )

        st.markdown(brief)          

    # ---------------------------
    # Generate Plan
    # ---------------------------

    st.divider()

    if st.button("📅 Generate Today's Plan"):

        plan = generate_daily_plan()

        plan = schedule_plan(
            plan,
            calendar_service
        )

        st.session_state["daily_plan"] = plan

        st.success(
            "Today's coaching schedule generated"
        )

    # ---------------------------
    # Show Plan
    # ---------------------------

    if "daily_plan" not in st.session_state:
        return

    plan = st.session_state["daily_plan"]

    # ---------------------------
    # Today
    # ---------------------------

    st.divider()
    st.header("📅 Today's Schedule")

    if len(plan["today"]) == 0:

        st.info(
            "No students scheduled today"
        )

    else:

        for student in plan["today"]:

            st.success(
                f"""
🕒 {student['time_slot']}

👤 Student: {student['student_id']}

📋 Session: {student['session_type']}

📝 Reason: {student['reason']}
"""
            )

    # ---------------------------
    # Deferred
    # ---------------------------

    if len(plan["deferred"]) > 0:

        st.header("⏳ Deferred To Tomorrow")

        for student in plan["deferred"]:

            st.info(
                f"""
👤 Student: {student['student_id']}

📝 Reason: {student['reason']}
"""
            )