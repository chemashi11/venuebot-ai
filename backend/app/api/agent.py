from fastapi import APIRouter
from pydantic import BaseModel
from app.agents.graph import agent_executor

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
def chat_with_agent(request: ChatRequest):
    # We pass the user's message to the LangGraph agent
    events = agent_executor.invoke({"messages": [("user", request.message)]})
    
    # The last message in the returned list is the AI's final response
    ai_reply = events["messages"][-1].content
    
    return {"reply": ai_reply}