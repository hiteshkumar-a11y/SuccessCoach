import pandas as pd
import streamlit as st

from src.student_data.google_sheet_service import signal_sheet


def show_dashboard():

    st.title("🚨 Coach Dashboard")

    records = signal_sheet.get_all_records()

    if not records:

        st.info("No alerts found")

        return

    df = pd.DataFrame(records)

    critical = len(
        df[df["severity"] == "CRITICAL"]
    )

    high = len(
        df[df["severity"] == "HIGH"]
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Critical Alerts",
        critical
    )

    col2.metric(
        "High Alerts",
        high
    )

    severity_order = {
        "CRITICAL": 4,
        "HIGH": 3,
        "MEDIUM": 2,
        "LOW": 1
    }

    df["priority"] = (
        df["severity"]
        .map(severity_order)
        .fillna(0)
    )

    # df = df.sort_values(
    #     "priority",
    #     ascending=False
    # )

    # Critical first
    # severity_order = {
    #     "CRITICAL": 4,
    #     "HIGH": 3,
    #     "MEDIUM": 2,
    #     "LOW": 1
    # }

    df["severity_score"] = (
        df["severity"]
        .map(severity_order)
        .fillna(0)
    )

    df = df.sort_values(
        by="severity_score",
        ascending=False
    )
    st.subheader("🚨 Immediate Action")

    immediate = df[
        df["urgency"].str.upper() == "IMMEDIATE"
    ]

    for _, row in immediate.iterrows():

        st.error(
            f"""
    Student: {row['student_id']}

    Signal: {row['signal_type']}

    {row['reason']}
    """
        )


    st.subheader("⚠️ High Priority")

    high = df[
        (df["severity"].str.upper() == "HIGH")
        &
        (df["urgency"].str.upper() != "IMMEDIATE")
    ]

    for _, row in high.iterrows():

        st.warning(
            f"""
    Student: {row['student_id']}

    Signal: {row['signal_type']}

    {row['reason']}
    """
        )


    st.subheader("📌 Monitor")

    monitor = df[
        df["severity"].str.upper() == "MEDIUM"
    ]

    for _, row in monitor.iterrows():

        st.info(
            f"""
    Student: {row['student_id']}

    Signal: {row['signal_type']}

    {row['reason']}
    """
        )