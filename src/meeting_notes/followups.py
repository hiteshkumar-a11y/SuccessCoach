from datetime import date

from src.student_data.google_sheet_service import (
    meeting_notes_sheet
)


def get_pending_followups():

    records = (
        meeting_notes_sheet
        .get_all_records()
    )

    pending = []

    today = date.today()

    for row in records:

        followup = row.get(
            "followup_date"
        )

        if not followup:
            continue

        pending.append(row)

    return pending