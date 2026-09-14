import Link from "next/link";

export default function HomePage() {
  return (
    <main>
      <section className="hero container">
        <p style={{ color: "var(--primary)", fontWeight: 800 }}>EDU AI QUIZ & Q&A</p>
        <h1>Học thông minh hơn với Quiz và trợ giảng AI</h1>
        <p>
          Tạo bộ câu hỏi theo chủ đề, luyện tập, nhận phản hồi tức thì và hỏi AI khi cần giải thích kiến thức.
        </p>
        <div className="actions">
          <Link className="btn btn-primary" href="/quiz">Tạo Quiz</Link>
          <Link className="btn btn-secondary" href="/qa">Hỏi AI</Link>
        </div>
      </section>

      <section className="section container">
        <div className="grid">
          <article className="card">
            <h3>AI Quiz Generator</h3>
            <p className="muted">Sinh câu hỏi trắc nghiệm theo chủ đề, độ khó và số lượng mong muốn.</p>
          </article>
          <article className="card">
            <h3>AI Q&A</h3>
            <p className="muted">Trợ giảng AI giải thích kiến thức và hỗ trợ học theo ngữ cảnh.</p>
          </article>
          <article className="card">
            <h3>Learning Analytics</h3>
            <p className="muted">Lưu lịch sử làm bài để theo dõi điểm số và tiến bộ.</p>
          </article>
        </div>
      </section>
    </main>
  );
}
