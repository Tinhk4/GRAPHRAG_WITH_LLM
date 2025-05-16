from langchain_community.graphs import Neo4jGraph
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_neo4j_connection():
    # Test connection
    print("Testing Neo4j connection...")
    try:
        graph = Neo4jGraph()
        print("✅ Successfully connected to Neo4j")
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return

    # Test basic queries
    print("\nTesting basic queries...")
    
    # 1. Count all nodes
    try:
        result = graph.query("MATCH (n) RETURN count(n) as count")
        print(f"Total nodes in database: {result[0]['count']}")
    except Exception as e:
        print(f"Error counting nodes: {str(e)}")

    # 2. Get all node labels
    try:
        result = graph.query("CALL db.labels()")
        print("\nNode labels in database:")
        for label in result:
            print(f"- {label['label']}")
    except Exception as e:
        print(f"Error getting labels: {str(e)}")

    # 3. Get sample nodes
    try:
        result = graph.query("MATCH (n) RETURN n LIMIT 5")
        print("\nSample nodes:")
        for node in result:
            print(f"- {node['n']}")
    except Exception as e:
        print(f"Error getting sample nodes: {str(e)}")

    # 4. Get relationships
    try:
        result = graph.query("MATCH ()-[r]->() RETURN DISTINCT type(r) as relationship_type")
        print("\nRelationship types:")
        for rel in result:
            print(f"- {rel['relationship_type']}")
    except Exception as e:
        print(f"Error getting relationships: {str(e)}")

    # 5. Get graph statistics
    try:
        result = graph.query("""
        MATCH (n)
        WITH count(n) as total_nodes
        MATCH ()-[r]->()
        WITH total_nodes, count(r) as total_relationships
        RETURN total_nodes, total_relationships
        """)
        stats = result[0]
        print("\nGraph Statistics:")
        print(f"Total nodes: {stats['total_nodes']}")
        print(f"Total relationships: {stats['total_relationships']}")
    except Exception as e:
        print(f"Error getting statistics: {str(e)}")

if __name__ == "__main__":
    test_neo4j_connection() 