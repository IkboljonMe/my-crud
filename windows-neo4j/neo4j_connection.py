from neo4j import GraphDatabase

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

neo4j_driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

try:
    with neo4j_driver.session() as session:
        session.run("RETURN 1")
    print("✅ Neo4j connection successful!")
except Exception as e:
    print("❌ Neo4j connection failed!")
    print(f"Error: {e}")

def get_neo4j_session():
    return neo4j_driver.session()
