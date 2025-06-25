from fastapi import FastAPI
from backend.view import router
import uvicorn
import os

os.environ["HTTPS_PROXY"] = "socks5://127.0.0.1:9090"
os.environ["HTTP_PROXY"] = "socks5://127.0.0.1:9090"

app = FastAPI(title="RAG Chatbot API")

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app="main:app", host="0.0.0.0", reload=True)