from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=2, max_length=4000)
    conversation_id: int | None = None


class AskResponse(BaseModel):
    answer: str
    conversation_id: int | None = None
