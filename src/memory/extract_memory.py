from src.llm.openai_client import llm

def extract_memory(text):
    prompt = f"""


Extract information that would be useful to remember about a student for future coaching conversations.

Remember things such as:

* goals
* interests
* aspirations
* future plans
* preferences
* learning habits
* recurring challenges
* motivations
* personal context

If the message contains nothing worth remembering, return NONE.

Student message:
{text}

Return only:

* the memory to store
  OR
* NONE
  """

    response = llm.invoke(prompt)

    memory = response.content.strip()

    if memory.upper() == "NONE":
        return None

    return memory
