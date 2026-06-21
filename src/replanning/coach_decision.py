def create_coach_decision(
    new_student,
    conflicting_students
):

    return {
        "coach_decision_required": True,
        "new_student": new_student,
        "conflicting_students": conflicting_students,
        "status": "PENDING"
    }