"use client";

import { useEffect, useState } from "react";
import { API_URL, Quiz } from "@/lib/api";

export default function QuizDetailPage({ params }: { params: Promise<{ id: string }> }) {
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [quizId, setQuizId] = useState<number | null>(null);
  const [answers, setAnswers] = useState<Record<number, number>>({});
  const [result, setResult] = useState<string>("");

  useEffect(() => {
    params.then(({ id }) => {
      const numericId = Number(id);
      setQuizId(numericId);
      fetch(`${API_URL}/quizzes/${numericId}`).then((r) => r.json()).then(setQuiz);
    });
  }, [params]);

  async function submit() {
    if (!quizId) return;
    const response = await fetch(`${API_URL}/quizzes/${quizId}/submit`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        answers: Object.entries(answers).map(([question_id, selected_index]) => ({
          question_id: Number(question_id),
          selected_index,
        })),
      }),
    });
    const data = await response.json();
    setResult(`Điểm: ${data.score}/100 · Đúng ${data.correct_count}/${data.total_questions}`);
  }

  if (!quiz) return <main className="section container">Đang tải...</main>;

  return (
    <main className="section container">
      <h1>{quiz.title}</h1>
      {quiz.questions.map((question, index) => (
        <section className="card" key={question.id} style={{ marginBottom: 16 }}>
          <h3>Câu {index + 1}. {question.content}</h3>
          {question.options.map((option, optionIndex) => (
            <label className="quiz-option" key={optionIndex}>
              <input
                type="radio"
                name={`q-${question.id}`}
                checked={answers[question.id] === optionIndex}
                onChange={() => setAnswers((prev) => ({ ...prev, [question.id]: optionIndex }))}
              />{" "}{option}
            </label>
          ))}
        </section>
      ))}
      <button className="btn btn-primary" onClick={submit}>Nộp bài</button>
      {result && <div className="card" style={{ marginTop: 16 }}><strong>{result}</strong></div>}
    </main>
  );
}
