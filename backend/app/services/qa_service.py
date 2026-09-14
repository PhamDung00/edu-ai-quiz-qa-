from sqlalchemy.ext.asyncio import AsyncSession

from app.models.conversation import Conversation, Message
from app.services.ai import ai_service


async def ask_and_save(
    db: AsyncSession,
    question: str,
    conversation_id: int | None,
    user_id: int | None,
) -> tuple[str, int]:
    conversation: Conversation | None = None
    if conversation_id:
        conversation = await db.get(Conversation, conversation_id)

    if conversation is None:
        conversation = Conversation(user_id=user_id, title=question[:80])
        db.add(conversation)
        await db.flush()

    db.add(Message(conversation_id=conversation.id, role="user", content=question))
    answer = await ai_service.answer(question)
    db.add(Message(conversation_id=conversation.id, role="assistant", content=answer))
    await db.commit()
    return answer, conversation.id
