from src.student_data.google_sheet_service import get_student_data
from src.retrieval.retriever import retrieve_context
from src.memory.memory_service import get_memory


def sheet_tool(student_id):
    return get_student_data(student_id)


def knowledge_tool(question):
    context = retrieve_context(question)

    if not context:
        return "NO_RELEVANT_CONTEXT_FOUND"

    return context


def memory_tool(student_id, question):
    memory = get_memory(student_id, question)

    if not memory:
        return "NO_MEMORY_FOUND"

    return memory


AVAILABLE_TOOLS = {
    "SHEET": sheet_tool,
    "KNOWLEDGE": knowledge_tool,
    "MEMORY": memory_tool
}