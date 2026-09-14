from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user_optional
from app.db.session import get_db
from app.models.user import User
from app.schemas.qa import AskRequest, AskResponse
from app.services.qa_service import ask_and_save

router = APIRouter()


@router.post("/ask", response_model=AskResponse)
async def ask(
    payload: AskRequest,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_current_user_optional),
) -> AskResponse:
    answer, conversation_id = await ask_and_save(
        db,
        payload.question,
        payload.conversation_id,
        user.id if user else None,
    )
    return AskResponse(answer=answer, conversation_id=conversation_id)
