from pymongo import MongoClient
import os

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

client = MongoClient(MONGO_DB_URL)

db = client["AFTABAI"]
collection = db["NetworkData"]

result = collection.update_many(
    {},
    {"$unset": {"index": ""}}
)

print(f"Modified {result.modified_count} documents")