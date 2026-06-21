from datetime import datetime


def create_calendar_event(
    service,
    student_id,
    session_type,
    reason,
    start_time,
    end_time
):

    event = {
        "summary": f"{session_type} - {student_id}",
        "description": reason,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "Asia/Kolkata"
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "Asia/Kolkata"
        }
    }

    try:

        response = service.events().insert(
            calendarId="hitesh.kumar@nxtwave.co.in",
            body=event
        ).execute()

        print("\n========== EVENT CREATED ==========")
        print("Student:", student_id)
        print("Session:", session_type)
        print("Event ID:", response.get("id"))
        print("Event Link:", response.get("htmlLink"))
        print("===================================\n")

        return True

    except Exception as e:

        print("\n========== CALENDAR ERROR ==========")
        print(e)
        print("====================================\n")

        return False