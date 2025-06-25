# 🤖 RAG Chatbot Application

This is a lightweight Retrieval-Augmented Generation (RAG) chatbot application that combines **semantic search** with **LLM-based answer generation**, using:

- ⚡ **FastAPI** for backend APIs  
- 📦 **pgvector** with PostgreSQL to store dense vector embeddings  
- 🧠 **MiniLM (all-MiniLM-L6-v2)** for embedding generation  
- 💬 **TinyLlama** or **Azure GPT-4o-mini** for response generation  
- 🌐 **Streamlit** for a simple and interactive frontend  
- 🧩 Modular **LangChain-style tools** for greetings, math, and web lookup  

---

## 🚀 Features

- 🔎 **Semantic Search** using pgvector + MiniLM embeddings  
- 🧠 **RAG Pipeline** retrieves relevant content and sends it to an LLM  
- 🧮 **Built-in Tools** for greeting, math (BODMAS), and simple web search  
- 🌐 **Streamlit UI** for real-time querying  
- 🔗 **FastAPI Backend** with clean routing  
- 🧠 **LangChain Agent** integrates tools and context-aware LLM responses  
- 🔐 Fully local setup (with optional Azure OpenAI support)  

---

## 🗂️ Project Structure

.
├── backend/
│ ├── main.py # FastAPI app entry point
│ ├── view.py # API route definitions
│ ├── stream.py # Streamlit frontend
│
├── tools/
│ ├── greeting_tool.py # Simple greeting handler
│ ├── bodmas_tool.py # Math solver (BODMAS)
│ └── web_search_tool.py # Web link tool (GitHub, YouTube, etc.)
│
├── agent.py # LangChain agent setup
├── llm_provider.py # Azure OpenAI or TinyLlama model setup
├── table.py # Ingests CSV and stores vector embeddings
├── similarity_search.py # Performs pgvector-based search
├── README.md # You're reading this :)
├── LICENSE # Project license
├── .env # 🔐 API keys and secrets (not tracked)
└── .gitignore # Ignores .env, pycache, etc.



---

## ⚙️ How to Run

1️⃣ Install Requirements: 
pip install -r requirements.txt

2️⃣ Start PostgreSQL with pgvector extension
Make sure your PostgreSQL DB has the vector extension installed:
CREATE EXTENSION IF NOT EXISTS vector;

3️⃣ Populate the Vector Database
Update the CSV path in table.py, then run:
python table.py

4️⃣ Run the FastAPI Backend
uvicorn backend.main:app --reload

5️⃣ Launch the Streamlit Frontend
streamlit run backend/stream.py

📦 Requirements
Python 3.10+

fastapi

streamlit

psycopg2

pgvector

sentence-transformers

torch

langchain

requests

openai (or Azure SDK for GPT-4o-mini)

📌 Notes
Embeddings use: sentence-transformers/all-MiniLM-L6-v2

LLM via: Azure GPT-4o-mini (replaceable with local TinyLlama or any other)

Proxy variables were removed for clean, universal use

Easily extensible with more tools or file types

🔐 Environment Setup
Create a .env file in the project root with your keys:
AZURE_API_KEY=your_azure_openai_key