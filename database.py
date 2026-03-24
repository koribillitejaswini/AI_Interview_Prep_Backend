from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["prepAI"]

users_collection = db["users"]
interview_collection = db["interviews"]