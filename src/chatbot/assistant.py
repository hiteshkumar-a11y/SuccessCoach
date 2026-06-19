from src.llm.openai_client import llm
from src.llm.prompt_template import PROMPT
from src.retrieval.query_rewriter import create_search_query

from src.memory.memory_service import (
    save_memory
)

from src.memory.extract_memory import (
    extract_memory
)

from src.agent.executor import gather_context

from src.session_memory.get_session import (
    get_recent_sessions
)


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

    # -------------------------
    # Conversation History
    # -------------------------
    conversation = ""

    for msg in chat_history[-10:]:

        conversation += (
            f"{msg['role'].upper()}: "
            f"{msg['content']}\n"
        )

    session_history = get_recent_sessions(
        student_id
    )

    # -------------------------
    # Follow-up Detection
    # -------------------------
    if question.strip().lower() in FOLLOW_UPS:

        question = f"""
This is a follow-up message.

Use the recent conversation history.

Student message:
{question}
"""

    # -------------------------
    # Retrieval Query
    # -------------------------
    search_query = f"""
Conversation:
{conversation}

Current Question:
{question}

The student may use:

- spelling mistakes
- abbreviations
- incomplete phrases
- informal language

Understand the intent.

Search using semantic meaning.

Examples:

website course
website related course
web development course

all refer to similar topics.

course timing
schedule
when is class

all refer to timing information.

Do not rely on exact keyword matching.
"""
    retrieval_query = create_search_query(question)
    # -------------------------
    # Agent Context Gathering
    # -------------------------
    context = gather_context(
        question=question,
        student_id=student_id
    )

    # -------------------------
    # Retrieved Context
    # -------------------------
    student_data = context.get(
        "student_data",
        ""
    )

    memory_context = context.get(
        "memory_context",
        ""
    )
    print("\nMEMORY CONTEXT:")
    print(memory_context)

    knowledge_context = context.get(
        "knowledge_context",
        ""
    )

    # Student Data Error Check
    if (
        isinstance(student_data, dict)
        and "error" in student_data
    ):
        return student_data["error"]

    if not knowledge_context:
        knowledge_context = (
            "NO_RELEVANT_CONTEXT_FOUND"
        )

    if not memory_context:
        memory_context = (
            "NO_MEMORY_FOUND"
        )

    # -------------------------
    # LLM Response
    # -------------------------
    chain = PROMPT | llm

    response = chain.invoke(
        {
            "student_data": student_data,
            "knowledge_context": knowledge_context,
             "memory_context": memory_context,
             "session_history": session_history,
             "conversation": conversation,
             "question": question
         }
    )

    answer = response.content

    # -------------------------
    # Save Memory
    # -------------------------

    memory = extract_memory(question)

    if memory:

        save_memory(
            student_id,
            memory
        )

    return answer