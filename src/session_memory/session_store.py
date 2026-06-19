import sqlite3

conn = sqlite3.connect(
    "session_memory.db",
    check_same_thread=False
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS session_summaries(
    id INTEGER PRIMARY KEY,
    student_id TEXT,
    summary TEXT
)
""")

conn.commit()