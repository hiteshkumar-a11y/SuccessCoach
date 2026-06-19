from src.memory.mem0_client import memory


def save_memory(student_id, text):

    try:

        memory.add(
            text,
            user_id=str(student_id)
        )

    except Exception as e:

        print("MEMORY SAVE ERROR:", e)


def get_memory(student_id, query):

    try:

        print("\n========== MEMORY SEARCH ==========")
        print("STUDENT:", student_id)
        print("QUERY:", query)

        results = memory.search(
            query=query,
            filters={
                "user_id": str(student_id)
            }
        )

        print("RESULT TYPE:", type(results))
        print("RAW RESULTS:", results)

        return str(results)

    except Exception as e:

        print("MEMORY SEARCH ERROR:", e)
        return ""

