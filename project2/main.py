import os

db_url = os.getenv("DATABASE_URL")
secret = os.getenv("API_SECRET_KEY")

print(f"Database URL: {db_url}")
print(f"API Secret: {secret}")
