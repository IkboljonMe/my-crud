import time
from db import get_mongo_collection

def update_book():
    collection = get_mongo_collection()
    
    start_time = time.time()
    collection.update_one({"title": "1984"}, {"$set": {"year": 1950}})
    print(f"🟢 Book updated successfully! Time Taken: {time.time() - start_time} seconds")

if __name__ == "__main__":
    update_book()
