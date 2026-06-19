from src.session_memory.session_store import cursor

def get_recent_sessions(
    student_id
):

    cursor.execute(
        """
        SELECT summary
        FROM session_summaries
        WHERE student_id=?
        ORDER BY id DESC
        LIMIT 5
        """,
        (student_id,)
    )

    rows = cursor.fetchall()

    return "\n".join(
        row[0]
        for row in rows
    )