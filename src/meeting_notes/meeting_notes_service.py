from datetime import datetime

from src.student_data.google_sheet_service import (
    meeting_notes_sheet
)


def save_meeting_note(
    student_id,
    discussion_summary,
    action_items,
    followup_date,
    risk_level
):

    meeting_notes_sheet.append_row(
        [
            student_id,
            datetime.now().strftime(
                "%Y-%m-%d"
            ),
            discussion_summary,
            action_items,
            followup_date,
            risk_level,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ]
    )


def get_student_notes(
    student_id
):

    records = (
        meeting_notes_sheet
        .get_all_records()
    )

    return [
        row
        for row in records
        if row["student_id"] == student_id
    ]