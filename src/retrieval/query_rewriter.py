# src/retrieval/query_rewriter.py

from src.llm.openai_client import llm

def create_search_query(question):
    prompt = f"""

Convert the student's question into a retrieval query.

Understand the student's intent.

Rules:

* Fix spelling mistakes.
* Expand abbreviations.
* Convert vague wording into searchable concepts.
* Include terms likely to appear in documents.
* Focus on retrieval, not answering.
* Return only the search query.

Question:
{question}
"""

    response = llm.invoke(prompt)

    return response.content.strip()
