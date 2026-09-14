from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user_optional
from app.db.session import get_db
from app.models.user import User
from app.schemas.quiz import (
    GenerateQuizRequest,
    QuizOut,
    SubmitQuizRequest,
    SubmitQuizResponse,
)
from app.services.quiz_service import generate_and_save_quiz, get_quiz, list_quizzes, submit_quiz

router = APIRouter()


@router.post("/generate", response_model=QuizOut, status_code=status.HTTP_201_CREATED)
async def generate_quiz(
    payload: GenerateQuizRequest,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_current_user_optional),
) -> QuizOut:
    quiz = await generate_and_save_quiz(db, payload, user.id if user else None)
    return QuizOut.model_validate(quiz)


@router.get("", response_model=list[QuizOut])
async def get_quizzes(db: AsyncSession = Depends(get_db)) -> list[QuizOut]:
    quizzes = await list_quizzes(db)
    return [QuizOut.model_validate(quiz) for quiz in quizzes]


@router.get("/{quiz_id}", response_model=QuizOut)
async def get_quiz_by_id(quiz_id: int, db: AsyncSession = Depends(get_db)) -> QuizOut:
    quiz = await get_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return QuizOut.model_validate(quiz)


@router.post("/{quiz_id}/submit", response_model=SubmitQuizResponse)
async def submit(
    quiz_id: int,
    payload: SubmitQuizRequest,
    db: AsyncSession = Depends(get_db),
    user: User | None = Depends(get_current_user_optional),
) -> SubmitQuizResponse:
    quiz = await get_quiz(db, quiz_id)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    attempt, results = await submit_quiz(db, quiz, payload, user.id if user else None)
    return SubmitQuizResponse(
        score=attempt.score,
        correct_count=sum(1 for item in results if item["is_correct"]),
        total_questions=attempt.total_questions,
        results=results,
    )
