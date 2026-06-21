from src.replanning.conflict_detector import (
    detect_conflict
)

from src.replanning.change_summary import (
    build_change_summary
)

from src.replanning.coach_decision import (
    create_coach_decision
)


SEVERITY_SCORE = {
    "CRITICAL": 4,
    "HIGH": 3,
    "MEDIUM": 2,
    "LOW": 1
}


def replan_if_needed(
    current_plan,
    new_signal
):

    new_priority = SEVERITY_SCORE.get(
        str(
            new_signal.get(
                "severity",
                ""
            )
        ).upper(),
        0
    )

    conflict = detect_conflict(
        current_plan,
        new_signal
    )

    if not conflict["conflict"]:

        current_plan["today"].append(
            {
                "student_id":
                new_signal["student_id"],

                "session_type":
                "Urgent Check-In",

                "reason":
                new_signal.get(
                    "coach_summary",
                    ""
                ),

                "priority_score":
                new_priority
            }
        )

        return {
            "updated_plan":
            current_plan,

            "summary":
            "Student added "
            "to today's plan.",

            "coach_decision_required":
            False
        }

    candidates = conflict["candidates"]

    highest_priority = max(
    s.get("priority_score", 0)
    for s in candidates
    )

    critical_students = [

    
    s

    for s in candidates

    if s.get(
        "priority_score",
        0
    ) >= 4
    

    ]

    # -------------------------

    # Coach decision required

    # -------------------------

    if (
    new_priority >= 4
    and
    len(critical_students) > 0
    ):

    
        decision = create_coach_decision(
            new_signal["student_id"],
            [
                s["student_id"]
                for s in critical_students
            ]
        )

        return {

            "updated_plan":
            current_plan,

            "summary":
            (
                "Multiple critical students "
                "need immediate support."
            ),

            "coach_decision_required":
            True,

            "decision":
            decision
        }
    

    # -------------------------

    # Automatic replacement

    # -------------------------

    lowest_priority_student = min(
    candidates,
    key=lambda s:
    s.get(
    "priority_score",
    0
    )
    )

    existing_priority = (
    lowest_priority_student.get(
    "priority_score",
    0
    )
    )

    current_plan["today"].remove(
      lowest_priority_student
    )
    current_plan["deferred"].append(
        candidate
    )
    current_plan["today"].append(
        {
            "student_id":
            new_signal["student_id"],
            "session_type":
            "Urgent Check-In",
            "reason":
            new_signal.get(
                "coach_summary",
                ""
            ),
            "priority_score":
            new_priority
        }
    )
    summary = build_change_summary(
        added_student=
        new_signal["student_id"],
        moved_student=
        lowest_priority_student["student_id"]
    )
    return {
        "updated_plan":
        current_plan,
        "summary":
        summary,
        "coach_decision_required":
        False
    }


    decision = create_coach_decision(
        new_signal["student_id"],
        [
            lowest_priority_student["student_id"]
        ]
    )

    return {
        "updated_plan":
        current_plan,

        "summary":
        "Coach decision required.",

        "coach_decision_required":
        True,

        "decision":
        decision
    }