from src.student_data.google_sheet_service import get_student_data
from src.retrieval.retriever import retrieve_context

from src.llm.openai_client import llm
from src.llm.prompt_template import PROMPT


FOLLOW_UPS = [
    "yes",
    "yess",
    "yeah",
    "ok",
    "okay",
    "tell me",
    "give me",
    "show me",
    "continue",
    "go ahead"
]


def get_answer(
    question,
    student_id,
    chat_history
):

    # Student Data
    student_data = get_student_data(student_id)

    if isinstance(student_data, dict):

        if "error" in student_data:
            return student_data["error"]

    # Knowledge Base Retrieval
    # knowledge_context = retrieve_context(question)
    
    
    # return (
    #     "I couldn't find information about that "
    #     "in the available learning materials "
    #     "or student records."
    # )

    # Build Conversation History
    conversation = ""

    for msg in chat_history[-10:]:

        conversation += (
            f"{msg['role'].upper()}: "
            f"{msg['content']}\n"
        )

    search_query = f"""
    Conversation:
    {conversation}

    Current Question:
    {question}
    """

    # search_query = f"""
    # Recent Conversation:
    # {conversation}

    # Current Question:
    # {question}

    Understand the student's intent.
    Ignore spelling mistakes and wording variations.
    Focus on the meaning of the question.
    """

    knowledge_context = retrieve_context(search_query)

    if not knowledge_context:
        knowledge_context = "NO_RELEVANT_CONTEXT_FOUND"

    # Follow-up detection
    if question.strip().lower() in FOLLOW_UPS:

        question = f"""
This is a follow-up message.

Use the recent conversation history to understand
what the student is referring to.

Student message:
{question}
"""

    # LangChain Chain
    chain = PROMPT | llm

    response = chain.invoke(
        {
            "student_data": student_data,
            "knowledge_context": knowledge_context,
            "conversation": conversation,
            "question": question
        }
    )

    return response.content
        