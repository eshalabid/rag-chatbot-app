import pandas as pd
import psycopg2
from sentence_transformers import SentenceTransformer
from pgvector.psycopg2 import register_vector

conn = psycopg2.connect(
    dbname="basf_db",
    user="root",
    password="root",
    host="127.0.0.1",
    port="5432"
)
register_vector(conn)
cur = conn.cursor()

cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
cur.execute("DROP TABLE IF EXISTS items;")
cur.execute("""
    CREATE TABLE items (
        id SERIAL PRIMARY KEY,
        ki_topic TEXT,
        ki_text TEXT,
        topic_embedding vector(384),
        text_embedding vector(384)
    );
""")
conn.commit()

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

csv_path = r'C:\Users\JUNCTION\Downloads\rag_sample_qas_from_kis.csv'
df = pd.read_csv(csv_path, usecols=["ki_topic", "ki_text"])

topics = df["ki_topic"].tolist()
texts = df["ki_text"].tolist()

topic_embeddings = model.encode(topics)
text_embeddings = model.encode(texts)

for i in range(len(df)):
    cur.execute("""
        INSERT INTO items (ki_topic, ki_text, topic_embedding, text_embedding)
        VALUES (%s, %s, %s, %s)
    """, (
        topics[i],
        texts[i],
        topic_embeddings[i].tolist(),
        text_embeddings[i].tolist()
    ))

conn.commit()
cur.close()
conn.close()
print("Table created and data inserted successfully.")
