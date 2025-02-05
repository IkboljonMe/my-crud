import time
from neo4j_connection import get_neo4j_session

def read_node():
    session = get_neo4j_session()
    start_time = time.time()
    result = session.run("MATCH (s:Student {student_number: 47563}) RETURN s")
    for record in result:
        print(f"📄 Node: {record['s']}")
    print(f"✅ Read Operation Time: {time.time() - start_time} seconds")
    session.close()

if __name__ == "__main__":
    read_node()
