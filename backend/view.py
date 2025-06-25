from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from tools.tool import agent

router = APIRouter(prefix="/api/chatbot")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

@router.post("/rag", response_model=QueryResponse)
async def get_rag_response(request: QueryRequest):
    try:
        response = agent.invoke({"input": request.query})
        print(response)
        return {"answer": response.get("output", "No response")}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


