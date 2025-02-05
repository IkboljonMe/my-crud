import time
from neo4j_connection import get_neo4j_session

def update_node():
    session = get_neo4j_session()
    start_time = time.time()
    session.run("MATCH (s:Student {student_number: 47563}) SET s.city = 'Ankara'")
    print(f"✅ Update Operation Time: {time.time() - start_time} seconds")
    session.close()

if __name__ == "__main__":
    update_node()
