export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000/api/v1";

export type QuizQuestion = {
  id: number;
  content: string;
  options: string[];
};

export type Quiz = {
  id: number;
  title: string;
  topic: string;
  difficulty: string;
  questions: QuizQuestion[];
};

export async function generateQuiz(input: {
  topic: string;
  difficulty: string;
  question_count: number;
}): Promise<Quiz> {
  const response = await fetch(`${API_URL}/quizzes/generate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input),
  });
  if (!response.ok) throw new Error("Không thể tạo quiz");
  return response.json();
}

export async function askAI(question: string, conversationId?: number | null) {
  const response = await fetch(`${API_URL}/qa/ask`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question, conversation_id: conversationId ?? null }),
  });
  if (!response.ok) throw new Error("Không thể nhận câu trả lời");
  return response.json() as Promise<{ answer: string; conversation_id: number }>;
}
