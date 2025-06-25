from similarity_search import similarity_search
from greeting_tool_fn import greeting_tool
from web_search_tool import web_tool
from bodmas_tool import bodmas_tool
from langchain.tools import Tool

def rag_tool_fn(query: str) -> str:
    results = similarity_search(query)
    return "\n\n".join([f"Topic: {r['topic']}\nText: {r['text']}" for r in results])

rag_tool = Tool(
    name="RAG Retriever",
    func=rag_tool_fn,
    description="Useful for retrieving relevant information from a document"
)

tools = [rag_tool,greeting_tool,bodmas_tool,web_tool]

