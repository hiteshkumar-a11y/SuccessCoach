from src.llm.openai_client import llm

def decide_tools(question): 
    prompt = f"""
    You are a routing agent.

    Your job is NOT to answer.

Your job is ONLY to decide which tool(s)
should be used.

---

AVAILABLE TOOLS

SHEET

Contains:

* student profile
* student name
* program
* cohort
* attendance
* marks
* scores
* exams
* academic records
* manager information

---

MEMORY

Contains:

* goals
* interests
* aspirations
* future plans
* preferences
* learning style
* recurring challenges
* personal facts shared earlier

---

KNOWLEDGE

Contains information from uploaded documents.

Examples:

* course details
* schedules
* certifications
* projects
* portal features
* setup instructions
* learning resources
* educational content
* platform documentation

---

ROUTING RULES

Understand the meaning.

Do not rely on exact keywords.

The user may:

* make spelling mistakes
* use abbreviations
* use incomplete phrases
* ask follow-up questions
* use informal language

Think about where the answer is most likely to exist.

---

EXAMPLES

Question:
"What is my attendance?"

Answer:
SHEET

---

Question:
"What am I studying?"

Answer:
SHEET

---

Question:
"What is my lowest score?"

Answer:
SHEET

---

Question:
"What are my goals?"

Answer:
MEMORY

---

Question:
"What did I say I want to learn next?"

Answer:
MEMORY

---

Question:
"What are my interests?"

Answer:
MEMORY

---

Question:
"What is the schedule for Build Your Own Responsive Website?"

Answer:
KNOWLEDGE

---

Question:
"Tell me about website related courses"

Answer:
KNOWLEDGE

---

Question:
"Is there anything about API setup?"

Answer:
KNOWLEDGE

---

Question:
"What should I learn after Data Science?"

Answer:
SHEET,MEMORY,KNOWLEDGE

---

Question:
"What is my lowest score and how can I improve?"

Answer:
SHEET,KNOWLEDGE

---

Question:
"What is Deep Learning?"

Answer:
KNOWLEDGE

---

Question:
"How do I drive a car?"

Answer:
NONE

---

IMPORTANT

Use multiple tools when needed.

If answer may exist in multiple tools,
return all relevant tools.

If question involves:

attendance
marks
scores
exams
student profile
current course

include SHEET.

If question involves:

goals
future plans
preferences
interests
things previously shared

include MEMORY.

If question involves:

courses
course schedules
certifications
projects
setup guides
portal features
learning materials
educational content

include KNOWLEDGE.

If the question is general knowledge
and does not require any tool:

return NONE.

---

Question:
{question}

Return ONLY:

SHEET
MEMORY
KNOWLEDGE
SHEET,MEMORY
SHEET,KNOWLEDGE
MEMORY,KNOWLEDGE
SHEET,MEMORY,KNOWLEDGE
NONE

No explanation.
"""


    response = llm.invoke(prompt)

    decision = (
        response.content
        .strip()
        .upper()
    )

    valid = {
        "SHEET",
        "MEMORY",
        "KNOWLEDGE",
        "SHEET,MEMORY",
        "SHEET,KNOWLEDGE",
        "MEMORY,KNOWLEDGE",
        "SHEET,MEMORY,KNOWLEDGE",
        "NONE"
    }

    if decision not in valid:
        return "KNOWLEDGE"

    return decision

