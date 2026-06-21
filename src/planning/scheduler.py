from datetime import datetime
from datetime import timedelta

from src.planning.calendar_service import (
    create_calendar_event
)


def schedule_plan(
    plan,
    calendar_service
):

    # start_time = datetime.now().replace(
    #     hour=9,
    #     minute=0,
    #     second=0,
    #     microsecond=0
    # )
    start_time = datetime.now() + timedelta(minutes=5)

    for student in plan["today"]:

        end_time = start_time + timedelta(
            minutes=30
        )

        create_calendar_event(
            service=calendar_service,
            student_id=student["student_id"],
            session_type=student["session_type"],
            reason=student["reason"],
            start_time=start_time,
            end_time=end_time
        )

        student["time_slot"] = (
            f"{start_time.strftime('%H:%M')} - "
            f"{end_time.strftime('%H:%M')}"
        )

        start_time = end_time

    return plan