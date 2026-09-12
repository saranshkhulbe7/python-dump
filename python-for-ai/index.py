import os

from dotenv import load_dotenv

load_dotenv("/.env")
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE", "default.db")
print(f"api_key: {api_key}")
print(f"database: {database}")
