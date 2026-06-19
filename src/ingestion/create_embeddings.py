import os

from src.ingestion.md_loader import load_markdown
from src.ingestion.text_splitter import split_text
from src.vectordb.chroma_manager import collection


def create_embeddings():

    docs_folder = "data/docs"

    all_chunks = []

    for file in os.listdir(docs_folder):

        if file.endswith(".md"):

            file_path = os.path.join(
                docs_folder,
                file
            )

            text = load_markdown(file_path)

            chunks = split_text(text)

            print(
                f"{file} -> {len(chunks)} chunks"
            )

            all_chunks.extend(chunks)

    try:

        existing = collection.get()

        if existing["ids"]:
            collection.delete(
                ids=existing["ids"]
            )

    except:
        pass

    print("\n===== SAMPLE CHUNKS =====")

    for chunk in all_chunks[:5]:
        print(chunk)
        print("----------------")

    collection.add(
        documents=all_chunks,
        ids=[
            f"chunk_{i}"
            for i in range(len(all_chunks))
        ]
    )

    print(
        f"Added {len(all_chunks)} chunks"
    )
if __name__ == "__main__":
    create_embeddings()