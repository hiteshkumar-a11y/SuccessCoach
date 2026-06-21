def build_change_summary(
    inserted_student,
    moved_student
):

    return (
        f"Student "
        f"{inserted_student} "
        f"was added to today's plan. "
        f"Student "
        f"{moved_student} "
        f"was moved to tomorrow "
        f"due to higher priority."
    )