import os
from dataclasses import dataclass

from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


@dataclass(frozen=True)
class Settings:
    qdrant_url: str
    qdrant_collection: str

    embedding_model: str
    chat_model: str

    retrieval_k: int


def get_settings() -> Settings:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is missing. Add it to your .env file.")

    return Settings(
        qdrant_url=os.getenv(
            "QDRANT_URL",
            "http://localhost:6333",
        ),
        qdrant_collection=os.getenv(
            "QDRANT_COLLECTION",
            "case-intelligence",
        ),
        embedding_model=os.getenv(
            "EMBEDDING_MODEL",
            "text-embedding-3-small",
        ),
        chat_model=os.getenv(
            "CHAT_MODEL",
            "gpt-4.1-mini",
        ),
        retrieval_k=int(os.getenv("RETRIEVAL_K", "6")),
    )
