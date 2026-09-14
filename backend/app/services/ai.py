import json

from openai import AsyncOpenAI

from app.core.config import settings


class AIService:
    def __init__(self) -> None:
        self.client = AsyncOpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

    async def generate_quiz(self, topic: str, difficulty: str, question_count: int) -> dict:
        if not self.client:
            return self._demo_quiz(topic, difficulty, question_count)

        prompt = f"""
Create a {difficulty} multiple-choice quiz about: {topic}.
Return exactly {question_count} questions.
Return JSON only with this schema:
{{
  "title": "string",
  "questions": [
    {{
      "content": "string",
      "options": ["A", "B", "C", "D"],
      "correct_index": 0,
      "explanation": "string"
    }}
  ]
}}
Rules:
- correct_index is zero-based.
- each question has exactly 4 options.
- explanations are concise and educational.
""".strip()

        response = await self.client.responses.create(
            model=settings.openai_model,
            input=prompt,
        )
        text = response.output_text.strip()
        if text.startswith("```"):
            text = text.strip("`")
            if text.startswith("json"):
                text = text[4:].strip()
        data = json.loads(text)
        return self._validate_quiz(data, question_count)

    async def answer(self, question: str, context: str = "") -> str:
        if not self.client:
            return (
                "Chế độ demo: chưa cấu hình OPENAI_API_KEY. "
                f"Câu hỏi của bạn là: {question}"
            )

        prompt = (
            "You are EDU AI, a concise educational tutor. "
            "Answer in Vietnamese unless the user asks for another language. "
            "Explain step-by-step when useful.\n\n"
            f"Context:\n{context or 'No external context provided.'}\n\n"
            f"Question:\n{question}"
        )
        response = await self.client.responses.create(model=settings.openai_model, input=prompt)
        return response.output_text.strip()

    @staticmethod
    def _validate_quiz(data: dict, expected_count: int) -> dict:
        questions = data.get("questions", [])
        if not isinstance(questions, list) or len(questions) != expected_count:
            raise ValueError("AI returned an invalid question count")
        for item in questions:
            options = item.get("options")
            correct_index = item.get("correct_index")
            if not isinstance(options, list) or len(options) != 4:
                raise ValueError("Each question must have exactly 4 options")
            if not isinstance(correct_index, int) or not 0 <= correct_index < 4:
                raise ValueError("Invalid correct_index")
        return data

    @staticmethod
    def _demo_quiz(topic: str, difficulty: str, question_count: int) -> dict:
        questions = []
        for i in range(question_count):
            questions.append(
                {
                    "content": f"Câu {i + 1}: Khái niệm nào liên quan nhất đến {topic}?",
                    "options": [
                        f"Khái niệm đúng về {topic}",
                        "Phương án nhiễu 1",
                        "Phương án nhiễu 2",
                        "Phương án nhiễu 3",
                    ],
                    "correct_index": 0,
                    "explanation": f"Đây là câu hỏi demo cho chủ đề {topic}.",
                }
            )
        return {"title": f"{topic} - {difficulty.title()}", "questions": questions}


ai_service = AIService()
