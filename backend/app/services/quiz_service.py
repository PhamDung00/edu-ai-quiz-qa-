from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.attempt import Attempt
from app.models.quiz import Question, Quiz
from app.schemas.quiz import GenerateQuizRequest, SubmitQuizRequest
from app.services.ai import ai_service


async def generate_and_save_quiz(
    db: AsyncSession,
    payload: GenerateQuizRequest,
    owner_id: int | None,
) -> Quiz:
    generated = await ai_service.generate_quiz(
        payload.topic,
        payload.difficulty,
        payload.question_count,
    )
    quiz = Quiz(
        title=generated.get("title", payload.topic),
        topic=payload.topic,
        difficulty=payload.difficulty,
        owner_id=owner_id,
    )
    quiz.questions = [
        Question(
            content=q["content"],
            options=q["options"],
            correct_index=q["correct_index"],
            explanation=q.get("explanation", ""),
        )
        for q in generated["questions"]
    ]
    db.add(quiz)
    await db.commit()
    await db.refresh(quiz)
    return await get_quiz(db, quiz.id)


async def list_quizzes(db: AsyncSession) -> list[Quiz]:
    result = await db.execute(
        select(Quiz).options(selectinload(Quiz.questions)).order_by(Quiz.created_at.desc())
    )
    return list(result.scalars().unique().all())


async def get_quiz(db: AsyncSession, quiz_id: int) -> Quiz | None:
    result = await db.execute(
        select(Quiz).where(Quiz.id == quiz_id).options(selectinload(Quiz.questions))
    )
    return result.scalar_one_or_none()


async def submit_quiz(
    db: AsyncSession,
    quiz: Quiz,
    payload: SubmitQuizRequest,
    user_id: int | None,
) -> tuple[Attempt, list[dict]]:
    questions = {question.id: question for question in quiz.questions}
    results: list[dict] = []
    correct = 0

    for answer in payload.answers:
        question = questions.get(answer.question_id)
        if not question:
            continue
        is_correct = answer.selected_index == question.correct_index
        correct += int(is_correct)
        results.append(
            {
                "question_id": question.id,
                "selected_index": answer.selected_index,
                "correct_index": question.correct_index,
                "is_correct": is_correct,
                "explanation": question.explanation,
            }
        )

    total = len(quiz.questions)
    score = round((correct / total) * 100, 2) if total else 0.0
    attempt = Attempt(
        quiz_id=quiz.id,
        user_id=user_id,
        score=score,
        total_questions=total,
        answers=[item.model_dump() for item in payload.answers],
    )
    db.add(attempt)
    await db.commit()
    await db.refresh(attempt)
    return attempt, results
