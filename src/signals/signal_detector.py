import json

from src.llm.openai_client import llm

def detect_signal(conversation):
    prompt = f"""
You are a Success Coach Risk Detection Agent.

Your task is to determine whether a coach should be notified.

Do NOT create signals for:

* normal learning questions
* concept explanations
* course information requests
* schedules
* attendance queries
* marks queries

Create a signal only when the conversation indicates:

* academic risk
* repeated poor performance
* stress
* burnout
* low motivation
* exam anxiety
* placement concerns
* time management issues
* career confusion
* financial concerns
* wellbeing concerns

Return JSON only.

coach_summary must be:

- 1 sentence
- max 20 words
- easy for a coach to understand quickly

Example:

"Student expressed hopelessness and difficulty coping with academic pressure."

Return:

{{
  "signal_detected": true,
  "signal_type": "",
  "severity": "",
  "urgency": "",
  "coach_summary": ""
}}
# {{
# "signal_detected": true,
# "signal_type": "",
# "severity": "",
# "urgency": "",
# "reason": ""
# }}


Conversation:

{conversation}
"""


    try:

        response = llm.invoke(prompt)

        return json.loads(
            response.content
        )

    except Exception as e:

        print(
            "SIGNAL ERROR:",
            e
        )

        return {
            "signal_detected": False
        }
