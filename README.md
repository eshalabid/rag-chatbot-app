# 🤖 RAG Chatbot Application

This is a lightweight RAG (Retrieval-Augmented Generation) chatbot application that combines semantic search with LLM-based answer generation using:

- **FastAPI** for backend APIs  
- **pgvector** with PostgreSQL to store dense vector embeddings  
- **MiniLM (all-MiniLM-L6-v2)** for embedding generation  
- **TinyLlama** and **Azure GPT-4o-mini** for natural language responses  
- **Streamlit** for an interactive frontend  
- Modular **LangChain-style tools** for greetings, math, and web lookup  

---

## 🚀 Features

- 🔎 **Semantic Search** using pgvector and MiniLM sentence embeddings  
- 🧠 **RAG Pipeline**: retrieves top relevant text chunks and sends them to an LLM  
- ⚙️ **Modular Tools**: includes greeting, BODMAS math solver, and web search tool  
- 🌐 **Streamlit UI** for easy querying  
- 🔗 **FastAPI Backend** for API endpoints  
- 🧩 Uses **LangChain Agent** for combining tools and generating dynamic answers  
- 🔐 Fully runs locally (except optional Azure GPT)  

---

## 🗂️ Project Structure

main.py → Launches FastAPI app
table.py → Inserts CSV data and vector embeddings into PostgreSQL
similarity_search.py → Embeds user query and retrieves similar content
rag_tool_agent.py → Combines RAG retrieval and passes to LLM for response
stream.py → Streamlit frontend
view.py → API routing logic
tool.py → Tool & agent setup with LangChain
greeting_tool_fn.py → Simple greeting tool
bodmas_tool.py → Math expression solver using BODMAS
web_search_tool.py → Simple website link search tool

---

## ⚙️ How to Run

### 🔧 1. Install Requirements
```bash
pip install -r requirements.txt
🗄️ 2. Start PostgreSQL with pgvector extension
Make sure your DB has pgvector installed and running.

🧠 3. Populate the vector DB
Edit the CSV path in table.py and run:
python table.py 

🚀 4. Run FastAPI backend
uvicorn main:app --reload

🌐 5. Run Streamlit frontend
streamlit run stream.py

📦 Requirements
Python 3.10+

FastAPI

Streamlit

psycopg2

pgvector

sentence-transformers

torch

langchain

requests

openai / Azure SDK (optional for GPT-4o-mini)

📌 Notes
Embeddings are generated using sentence-transformers/all-MiniLM-L6-v2

Azure OpenAI (GPT-4o-mini) is used in agent setup, but can be swapped for TinyLlama

Proxy is used for some environments — remove if not needed

Can be extended with more tools or document types

