import time
from db import get_neo4j_session

def delete_book():
    session = get_neo4j_session()
    start_time = time.time()
    session.run("MATCH (b:Book {title: '1984'}) DELETE b")
    print(f"🟢 Book Deleted Successfully! 🕒 Time Taken: {time.time() - start_time} seconds")
    session.close()

if __name__ == "__main__":
    delete_book()
