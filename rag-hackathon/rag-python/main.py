import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import (
    Docx2txtLoader,
    PyPDFLoader,
    TextLoader,
)
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.documents import Document
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient

# env setup

print("\n" + "=" * 80)
print("1. LOADING ENVIRONMENT VARIABLES")
print("=" * 80)

load_dotenv(find_dotenv())

openai_api_key = os.environ["OPENAI_API_KEY"]

qdrant_api_key = os.environ["QDRANT_API_KEY"]

qdrant_url = os.environ["QDRANT_URL"]

qdrant_collection = os.getenv(
    "QDRANT_COLLECTION",
    "case-intelligence",
)

print("OPENAI_API_KEY loaded:", bool(openai_api_key))
print("QDRANT_API_KEY loaded:", bool(qdrant_api_key))
print("Qdrant URL:", qdrant_url)
print("Collection:", qdrant_collection)


# openai client setup

print("\n" + "=" * 80)
print("2. CREATING OPENAI CLIENTS")
print("=" * 80)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

chat_model = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
)

print("Embedding model created")
print("Chat model created")


print("\n" + "=" * 80)
print("3. CONNECTING TO QDRANT")
print("=" * 80)

qdrant_client = QdrantClient(
    url=qdrant_url,
    api_key=qdrant_api_key,
)

collections = qdrant_client.get_collections()

print("Connected to Qdrant")
print("Existing collections:")

for collection in collections.collections:
    print("-", collection.name)


print("\n" + "=" * 80)
print("4. FINDING DATA FILES")
print("=" * 80)

data_dir = Path("data")

documents_dir = data_dir / "documents"
transcripts_dir = data_dir / "transcripts"

print("Documents directory:", documents_dir)
print("Transcripts directory:", transcripts_dir)
