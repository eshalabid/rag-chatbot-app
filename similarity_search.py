import psycopg2
from pgvector.psycopg2 import register_vector
from sentence_transformers import SentenceTransformer

DB_CONFIG = {
    "dbname": "basf_db",
    "user": "root",
    "password": "root",
    "host": "127.0.0.1",
    "port": "5432"
}
TOP_K = 3

def similarity_search(query):
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    query_embedding = model.encode(query)

    conn = psycopg2.connect(**DB_CONFIG)
    register_vector(conn)
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            ki_topic,
            ki_text,
            (topic_embedding <#> %s) AS sim_topic,
            (text_embedding <#> %s) AS sim_text
        FROM items
        ORDER BY ((topic_embedding <#> %s) + (text_embedding <#> %s)) ASC
        LIMIT %s;
    """, (query_embedding, query_embedding, query_embedding, query_embedding, TOP_K))

    results = cur.fetchall()
    cur.close()
    conn.close()

    retrieved_chunks = []
    for topic, text, sim_t, sim_b in results:
        retrieved_chunks.append({
            "topic": topic,
            "text": text,
            "similarity_score": round((2 - (sim_t + sim_b)) / 2, 4)
        })

    return retrieved_chunks

def greeting_tool_fn(_:str) -> str:
    return "Helloo! Im your assistant. How can i help you today :)?"


def web_search_tool(query:str) -> str:
    eb_links = {
        "linkedin": "https://www.linkedin.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://stackoverflow.com",
        "openai": "https://www.openai.com",
        "youtube": "https://www.youtube.com",
    }
    query_lower = query.lower()
    for name, link in eb_links.items():
        if name in query_lower:
            return f"Here’s the link to {name.title()}: {link}"
    return "Sorry, I couldn’t find a matching website in my list."


def bodmas_tool_fn(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return f"The result of '{expression}' is {result}"
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"

if __name__ == "__main__":
    query ="How do I set up my company email on my mobile device"
    top_docs = similarity_search(query)

    print("\n🔍 Top Results:")
    print(top_docs)

