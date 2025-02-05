import time
from db import get_neo4j_session

def add_book():
    session = get_neo4j_session()
    start_time = time.time()
    session.run("CREATE (b:Book {title: '1984', author: 'George Orwell', year: 1949})")
    print(f"🟢 Book Added Successfully! 🕒 Time Taken: {time.time() - start_time} seconds")
    session.close()

if __name__ == "__main__":
    add_book()
