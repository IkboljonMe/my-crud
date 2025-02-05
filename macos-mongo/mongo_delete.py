import time
from mongo_connection import get_mongo_collection

def delete_document():
    collection = get_mongo_collection()
    
    start_time = time.time()
    collection.delete_one({"student_number": 47563})
    print(f"Delete Operation Time: {time.time() - start_time} seconds")

if __name__ == "__main__":
    delete_document()
