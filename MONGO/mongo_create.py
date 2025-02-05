import time
from db import get_mongo_collection

def add_book():
    collection = get_mongo_collection()
    book = {"title": "1984", "author": "George Orwell", "year": 1949}
    
    start_time = time.time()
    collection.insert_one(book)
    print(f"🟢 Book Added Successfully! 🕒 Time Taken: {time.time() - start_time} seconds")

if __name__ == "__main__":
    add_book()
