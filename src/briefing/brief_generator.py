from src.llm.openai_client import llm
from src.briefing.brief_prompt import BRIEF_PROMPT

from src.student_data.google_sheet_service import (
    get_student_data,
    signal_sheet
)

from src.memory.memory_service import get_memory


def generate_student_brief(student_id):

    student_data = get_student_data(
        student_id
    )

    profile = student_data.get(
        "profile",
        {}
    )

    memories = get_memory(
        student_id,
        "student summary"
    )

    signals = [
        row
        for row in signal_sheet.get_all_records()
        if row.get("student_id") == student_id
    ]

    student_context = {
        "name": profile.get("name", ""),
        "program": profile.get("program", ""),
        "cohort": profile.get("cohort", ""),
        "recent_signals": signals[-3:],
        "memory": memories
    }

    prompt = BRIEF_PROMPT.format(
        student_context=student_context
    )

    response = llm.invoke(prompt)

    return response.content