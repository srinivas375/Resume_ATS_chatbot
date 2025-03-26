import pymongo
from pymongo.errors import DuplicateKeyError

try:
    conn = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS = 5000)
    conn.admin.command('ping')
    print("Connected to mongodb successfully")
    
    db = conn["demo"]
    collection = db["student"]
    collection.create_index("email", unique = True)
    
except pymongo.errors.ServerSelectionTimeoutError as e:
    print("MongoDB connection failed:", e)
    