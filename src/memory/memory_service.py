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

        # return str(results)
        memories = []

        for item in results.get("results", []):

            memory_text = item.get("memory")

            if memory_text:
                memories.append(memory_text)

        return "\n".join(memories)

    except Exception as e:

        print("MEMORY SEARCH ERROR:", e)
        return ""

