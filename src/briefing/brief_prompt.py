BRIEF_PROMPT = """
You are generating a PRE-MEETING COACH BRIEF.

The coach needs a 30-second summary before speaking with the student.


The brief is for a coach who needs a quick understanding of the student before a conversation.

Student Context:
{student_context}



Do NOT provide coaching advice.

Do NOT tell the coach what actions to take.

Do NOT provide recommendations, interventions, or instructions.

Focus only on relevant student context.

Return exactly:

## Student Snapshot

(2-4 sentences)

## Recent Context

(3-6 bullet points)

## Things To Keep In Mind

(3-5 bullet points)

Keep the entire brief under 150 words.

Only include information that is relevant to today's conversation.
Ignore attendance percentages, detailed marks, exam lists, and other administrative details unless they directly relate to the student's current situation.


"""