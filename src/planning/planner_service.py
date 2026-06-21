import json

from src.llm.openai_client import llm
from src.planning.planner_prompt import PLANNER_PROMPT


def create_plan(signals):

    try:

        chain = PLANNER_PROMPT | llm

        response = chain.invoke(
            {
                "signals": signals
            }
        )

        return json.loads(
            response.content
        )

    except Exception as e:

        print(
            "PLANNER ERROR:",
            e
        )

        return {
            "today": [],
            "deferred": []
        }