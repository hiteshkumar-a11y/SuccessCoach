from src.student_data.google_sheet_service import get_student_data
from src.llm.openai_client import client
from src.config.settings import CHAT_MODEL


def get_answer(question, student_id):

    student_data = get_student_data(student_id)

    if not student_data:
        return f"Student ID {student_id} not found."

    if isinstance(student_data, dict) and "error" in student_data:
        return student_data["error"]

    prompt = f"""
{STUDENT_ASSISTANT_PROMPT}

Student Data:
{student_data}

Student Question:
{question}

Instructions:
- Answer using only the student data provided.
- Do not make up information.
- If information is missing, clearly mention it.
- Mention attendance when relevant.
- Mention marks when relevant.
- Highlight low attendance (below 75%).
- Give short and actionable suggestions.
"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content