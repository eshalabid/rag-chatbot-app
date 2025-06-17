from langchain.agents import initialize_agent, AgentType
from langchain_openai import AzureChatOpenAI
from similarity_search import similarity_search
from langchain.tools import Tool
import os

COMPLETION_AZURE_OPENAI_KEY = "a5e5ac8242f84009bc9b527a269dd3fa"
COMPLETION_API_VERSION = "2024-08-01-preview"
COMPLETION_AZURE_OPENAI_ENDPOINT = "https://basf-open-ai.openai.azure.com/"
COMPLETION_LLM_COMPLETION_MODEL_NAME = "gpt-4o-mini"
COMPLETION_DEPLOYMENT_NAME = "basf-rag-gpt4o-mini-ai"

os.environ["HTTPS_PROXY"] = "socks5://127.0.0.1:9090"
os.environ["HTTP_PROXY"] = "socks5://127.0.0.1:9090"

def rag_tool_fn(query: str) -> str:
    results = similarity_search(query)
    return "\n\n".join([f"Topic: {r['topic']}\nText: {r['text']}" for r in results])

rag_tool = Tool(
    name="RAG Retriever",
    func=rag_tool_fn,
    description="Useful for retrieving relevant information from a document"
)

llm = AzureChatOpenAI(
    api_key=COMPLETION_AZURE_OPENAI_KEY,
    api_version=COMPLETION_API_VERSION,
    azure_endpoint=COMPLETION_AZURE_OPENAI_ENDPOINT,
    deployment_name=COMPLETION_DEPLOYMENT_NAME,
    model_name=COMPLETION_LLM_COMPLETION_MODEL_NAME,
)

tools = [rag_tool]
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

if __name__ == "__main__":
    query = "How do I set up my company email on my mobile device?"
    response = agent.invoke({"input": query})
    print("\n🤖 Agent's Answer:\n", response.get("output"))
