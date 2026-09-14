import Link from "next/link";

export function Nav() {
  return (
    <nav className="nav">
      <Link className="brand" href="/">EDU AI</Link>
      <div className="navlinks">
        <Link href="/dashboard">Dashboard</Link>
        <Link href="/quiz">Quiz</Link>
        <Link href="/qa">AI Q&A</Link>
        <Link href="/login">Đăng nhập</Link>
      </div>
    </nav>
  );
}
