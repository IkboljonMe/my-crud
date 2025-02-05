import time
from mongo_connection import get_mongo_collection

def read_document():
    collection = get_mongo_collection()
    
    start_time = time.time()
    student = collection.find_one({"student_number": 47563})
    print(f"Read Operation Time: {time.time() - start_time} seconds")
    print(f"Document: {student}")

if __name__ == "__main__":
    read_document()
