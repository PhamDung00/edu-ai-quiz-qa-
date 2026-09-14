from fastapi import APIRouter

from app.api.v1.routes import auth, health, qa, quizzes

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(quizzes.router, prefix="/quizzes", tags=["quizzes"])
api_router.include_router(qa.router, prefix="/qa", tags=["qa"])
