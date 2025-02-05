import time
from db import get_neo4j_session

def update_book():
    session = get_neo4j_session()
    start_time = time.time()
    session.run("MATCH (b:Book {title: '1984'}) SET b.year = 1950")
    print(f"🟢 Book Updated Successfully! 🕒 Time Taken: {time.time() - start_time} seconds")
    session.close()

if __name__ == "__main__":
    update_book()
