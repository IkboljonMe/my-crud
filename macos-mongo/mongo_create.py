import time
from mongo_connection import get_mongo_collection

def create_document():
    collection = get_mongo_collection()
    student = {"name": "Oguzhan Yazdicutan", "student_number": 47563, "city": "Istanbul"}
    
    start_time = time.time()
    collection.insert_one(student)
    print(f"Create Operation Time: {time.time() - start_time} seconds")

if __name__ == "__main__":
    create_document()
