from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://Oguzhan:hvcWGR9EuktcT0aX@oguzhancluster.wrtrm.mongodb.net/?retryWrites=true&w=majority&appName=OguzhanCluster"
MONGO_DB_NAME = "uehs"
MONGO_COLLECTION_NAME = "students"

try:
    mongo_client = MongoClient(MONGO_URI)
    mongo_db = mongo_client[MONGO_DB_NAME]
    mongo_collection = mongo_db[MONGO_COLLECTION_NAME]

    # Test the connection
    mongo_client.admin.command('ping')
    print("✅ MongoDB connection successful!")
    print(f"🔗 Connected to database: {MONGO_DB_NAME}, collection: {MONGO_COLLECTION_NAME}")

except Exception as e:
    print("❌ MongoDB connection failed!")
    print(f"Error: {e}")

def get_mongo_collection():
    return mongo_collection
