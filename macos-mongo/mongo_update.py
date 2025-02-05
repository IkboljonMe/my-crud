import time
from mongo_connection import get_mongo_collection

def update_document():
    collection = get_mongo_collection()
    
    start_time = time.time()
    collection.update_one({"student_number": 47563}, {"$set": {"city": "Ankara"}})
    print(f"Update Operation Time: {time.time() - start_time} seconds")

if __name__ == "__main__":
    update_document()
