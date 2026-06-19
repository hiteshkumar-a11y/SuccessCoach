from src.agent.router import decide_tools

from src.agent.tools import (
sheet_tool,
knowledge_tool,
memory_tool
)

from src.retrieval.query_rewriter import (
create_search_query
)

def gather_context(question, student_id):
    tools = decide_tools(question)

    print("\nTOOLS SELECTED:", tools)

    student_data = ""  
    memory_context = ""
    knowledge_context = ""

# Create retrieval query only for RAG
    retrieval_query = create_search_query(
        question
    )

    if "SHEET" in tools:
        student_data = sheet_tool(
            student_id
        )

    if "MEMORY" in tools:
        memory_context = memory_tool(
            student_id,
            question
        )

    if "KNOWLEDGE" in tools:
        knowledge_context = knowledge_tool(
            retrieval_query
        )

    return {
        "student_data": student_data,
        "memory_context": memory_context,
        "knowledge_context": knowledge_context
    }

