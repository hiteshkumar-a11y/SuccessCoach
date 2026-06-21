def detect_conflict(
    current_plan,
    new_signal
):

    today_students = current_plan.get(
        "today",
        []
    )

    if len(today_students) < 8:
        return {
            "conflict": False
        }

    lowest_student = min(
        today_students,
        key=lambda x: x.get(
            "priority_score",
            0
        )
    )

    return {
        "conflict": True,
        "candidate": lowest_student
    }