from src.llm.openai_client import llm

def summarize_session(
    conversation
):

    prompt = f"""
Summarize this session.

Include:

- topics discussed
- goals
- interests
- decisions

Conversation:

{conversation}
"""

    return llm.invoke(
        prompt
    ).content