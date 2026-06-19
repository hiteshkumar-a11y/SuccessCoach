from src.vectordb.chroma_manager import collection


def retrieve_context(question):

    results = collection.query(
        query_texts=[question],
        n_results=6
    )

    docs = results["documents"][0]

    print("\nQUERY:")
    print(question)

    print("\nRETRIEVED DOCS:")
    for doc in docs:
        print(doc[:300])
        print("-" * 50)

    if len(docs) == 0:
        return None

    return "\n\n".join(docs)