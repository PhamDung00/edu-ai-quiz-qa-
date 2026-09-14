from pydantic import BaseModel, Field


class GenerateQuizRequest(BaseModel):
    topic: str = Field(min_length=2, max_length=200)
    difficulty: str = Field(default="medium", pattern="^(easy|medium|hard)$")
    question_count: int = Field(default=5, ge=1, le=20)


class QuestionOut(BaseModel):
    id: int
    content: str
    options: list[str]

    model_config = {"from_attributes": True}


class QuizOut(BaseModel):
    id: int
    title: str
    topic: str
    difficulty: str
    questions: list[QuestionOut]

    model_config = {"from_attributes": True}


class AnswerIn(BaseModel):
    question_id: int
    selected_index: int = Field(ge=0)


class SubmitQuizRequest(BaseModel):
    answers: list[AnswerIn]


class QuestionResult(BaseModel):
    question_id: int
    selected_index: int
    correct_index: int
    is_correct: bool
    explanation: str


class SubmitQuizResponse(BaseModel):
    score: float
    correct_count: int
    total_questions: int
    results: list[QuestionResult]
