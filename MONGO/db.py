from pymongo import MongoClient

# 🌐 MongoDB Connection Details
MONGO_URI = "mongodb+srv://batuhan:sGGXrN8BFpgUj1vY@batuhan.qfzmy.mongodb.net/?retryWrites=true&w=majority&appName=batuhan"
MONGO_DB_NAME = "library"
MONGO_COLLECTION_NAME = "books"

try:
    mongo_client = MongoClient(MONGO_URI)
    mongo_db = mongo_client[MONGO_DB_NAME]
    mongo_collection = mongo_db[MONGO_COLLECTION_NAME]

    # 🟢Test Connection
    mongo_client.admin.command('ping')
    print("🟢 MongoDB Connected Successfully!")
    print(f"📚 Database: {MONGO_DB_NAME}, Collection: {MONGO_COLLECTION_NAME}")

except Exception as e:
    print("🔴 MongoDB Connection Failed!")
    print(f"⚠️ Error: {e}")

def get_mongo_collection():
    return mongo_collection
