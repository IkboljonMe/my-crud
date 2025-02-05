import time
from neo4j_connection import get_neo4j_session

def create_node():
    session = get_neo4j_session()
    start_time = time.time()
    session.run("CREATE (s:Student {name: 'Oguzhan Yazdicutan', student_number: 47563, city: 'Istanbul'})")
    print(f"✅ Create Operation Time: {time.time() - start_time} seconds")
    session.close()

if __name__ == "__main__":
    create_node()
