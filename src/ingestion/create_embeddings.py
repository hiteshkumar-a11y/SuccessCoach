from src.llm.openai_client import client
from src.config.settings import EMBEDDING_MODEL


def get_embedding(text: str):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text
    )

    return response.data[0].embedding