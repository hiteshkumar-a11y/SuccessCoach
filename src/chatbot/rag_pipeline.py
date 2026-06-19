from src.student_data.google_sheet_service import get_student_data
from src.llm.openai_client import client
from src.config.settings import CHAT_MODEL


def get_answer(question, student_id):

    student_data = get_student_data(student_id)

    if "error" in student_data:
        return student_data["error"]

    prompt = f"""
Student Data:
{student_data}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a Student Success Coach."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content