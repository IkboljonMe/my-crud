import time
from db import get_mongo_collection

def delete_book():
    collection = get_mongo_collection()
    
    start_time = time.time()
    collection.delete_one({"title": "1984"})
    print(f"🟢 Book deleted successfully! Time Taken: {time.time() - start_time} seconds")

if __name__ == "__main__":
    delete_book()
