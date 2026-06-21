from src.student_data.google_sheet_service import signal_sheet

from datetime import datetime

def add_signal(
student_id,
signal_type,
severity,
urgency,
reason,
coach_summary
):


    signal_sheet.append_row(
        [
            student_id,
            signal_type,
            severity,
            urgency,
            coach_summary
            reason,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            "FALSE"
        ]
    )

