from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional

class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1)
    history: List[Dict[str, Any]] = Field(default_factory=list)

class ChatResponse(BaseModel):
    answer: str
    sources: List[Dict[str, Any]] = Field(default_factory=list)

class StatusResponse(BaseModel):
    status: str
    detail: Optional[str] = None
