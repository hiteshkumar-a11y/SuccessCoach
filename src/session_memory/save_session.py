from src.session_memory.session_store import (
    conn,
    cursor
)

def save_session_summary(
    student_id,
    summary
):

    cursor.execute(
        """
        INSERT INTO session_summaries
        (
            student_id,
            summary
        )
        VALUES (?,?)
        """,
        (
            student_id,
            summary
        )
    )

    conn.commit()