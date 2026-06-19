from src.student_data.google_sheet_service import get_student_data
from src.retrieval.retriever import retrieve_context
from src.llm.openai_client import client
from src.llm.prompt_template import SYSTEM_PROMPT
from src.config.settings import CHAT_MODEL


def get_answer(question, student_id, chat_history):

    student_data = get_student_data(student_id)

    knowledge_context = retrieve_context(question)

    if not knowledge_context:
        knowledge_context = "NO_RELEVANT_CONTEXT_FOUND"

    conversation = ""

    for msg in chat_history[-10:]:
        conversation += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
Student Information:
{student_data}

Knowledge Base Context:
{knowledge_context}

Conversation History:
{conversation}

Current Student Message:
{question}
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