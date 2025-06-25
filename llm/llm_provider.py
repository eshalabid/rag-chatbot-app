import os
from langchain_openai import AzureChatOpenAI

llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version="2024-08-01-preview",
    azure_endpoint="https://basf-open-ai.openai.azure.com/",
    deployment_name="basf-rag-gpt4o-mini-ai",
    model_name="gpt-4o-mini"
)