"use client";

import { FormEvent, useState } from "react";
import Link from "next/link";
import { generateQuiz, Quiz } from "@/lib/api";

export default function QuizPage() {
  const [topic, setTopic] = useState("Python cơ bản");
  const [difficulty, setDifficulty] = useState("medium");
  const [count, setCount] = useState(5);
  const [quiz, setQuiz] = useState<Quiz | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function onSubmit(event: FormEvent) {
    event.preventDefault();
    setLoading(true);
    setError("");
    try {
      setQuiz(await generateQuiz({ topic, difficulty, question_count: count }));
    } catch (err) {
      setError(err instanceof Error ? err.message : "Có lỗi xảy ra");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="section container">
      <h1>Tạo Quiz bằng AI</h1>
      <p className="muted">Chọn chủ đề, mức độ và số lượng câu hỏi.</p>
      <form className="form card" onSubmit={onSubmit}>
        <label>
          Chủ đề
          <input className="input" value={topic} onChange={(e) => setTopic(e.target.value)} />
        </label>
        <label>
          Độ khó
          <select className="input" value={difficulty} onChange={(e) => setDifficulty(e.target.value)}>
            <option value="easy">Easy</option>
            <option value="medium">Medium</option>
            <option value="hard">Hard</option>
          </select>
        </label>
        <label>
          Số câu
          <input className="input" type="number" min={1} max={20} value={count} onChange={(e) => setCount(Number(e.target.value))} />
        </label>
        <button className="btn btn-primary" disabled={loading}>{loading ? "Đang tạo..." : "Tạo Quiz"}</button>
        {error && <p>{error}</p>}
      </form>

      {quiz && (
        <section className="section">
          <div className="card">
            <h2>{quiz.title}</h2>
            <p className="muted">{quiz.questions.length} câu · {quiz.difficulty}</p>
            <Link className="btn btn-primary" href={`/quiz/${quiz.id}`}>Bắt đầu làm bài</Link>
          </div>
        </section>
      )}
    </main>
  );
}
