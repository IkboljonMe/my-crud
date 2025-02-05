import time
from db import get_mongo_collection

def get_books():
    collection = get_mongo_collection()
    
    start_time = time.time()
    books = list(collection.find({}))
    print(f"📚 Books in collection (Time Taken: {time.time() - start_time} seconds):")
    for book in books:
        print(book)

if __name__ == "__main__":
    get_books()
