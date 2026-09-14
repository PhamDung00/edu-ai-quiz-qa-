export default function DashboardPage() {
  return (
    <main className="section container">
      <h1>Dashboard</h1>
      <p className="muted">Tổng quan kết quả học tập. Dữ liệu thật sẽ được nối ở sprint analytics.</p>
      <div className="grid">
        <div className="card"><span className="muted">Quiz đã làm</span><div className="stat">0</div></div>
        <div className="card"><span className="muted">Điểm trung bình</span><div className="stat">--</div></div>
        <div className="card"><span className="muted">Chuỗi học tập</span><div className="stat">0 ngày</div></div>
      </div>
    </main>
  );
}
