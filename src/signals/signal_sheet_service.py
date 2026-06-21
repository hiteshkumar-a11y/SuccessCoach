from src.student_data.google_sheet_service import signal_sheet

from datetime import datetime

def add_signal(
student_id,
signal_type,
severity,
urgency,
reason,
coach_summary,
planned,
planned_date,
timestamp,
actioned,
calendar_service.py
):


    signal_sheet.append_row(
        [
            student_id,
            signal_type,
            severity,
            urgency,
            coach_summary
            reason,
            planned,
            timestamp,
            actioned,
            planned_date,
            calendar_service.py
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "FALSE"
        ]
    )

