from src.student_data.google_sheet_service import get_student_data
from src.llm.openai_client import client
from src.llm.prompt_template import SYSTEM_PROMPT
from src.config.settings import CHAT_MODEL


def get_answer(question, student_id,chat_history):

    student_data = get_student_data(student_id)
    conversation = ""

    for msg in chat_history[-10:]:
        conversation += (
        f"{msg['role']}: "
        f"{msg['content']}\n"
        )

    if not student_data:
        return "Student not found."

    if "error" in student_data:
        return student_data["error"]


    

    prompt = f"""
    Student Profile:
    {student_data}

    Conversation History:
    {conversation}

    Current Message:
    {question}

    First understand the student's intent.

    Use student data only if it helps answer the question.

    Do not automatically discuss scores, attendance, or exams.

    Respond like a mentor talking to a student.
    """

    response = client.chat.completions.create(
        model=CHAT_MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content