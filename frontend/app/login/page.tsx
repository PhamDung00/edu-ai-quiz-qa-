"use client";

import { FormEvent, useState } from "react";
import { API_URL } from "@/lib/api";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  async function submit(event: FormEvent) {
    event.preventDefault();
    const response = await fetch(`${API_URL}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });
    const data = await response.json();
    if (response.ok) {
      localStorage.setItem("edu_ai_token", data.access_token);
      setMessage("Đăng nhập thành công.");
    } else {
      setMessage(data.detail ?? "Đăng nhập thất bại.");
    }
  }

  return (
    <main className="section container">
      <div className="card" style={{ maxWidth: 520, margin: "40px auto" }}>
        <h1>Đăng nhập</h1>
        <form className="form" onSubmit={submit}>
          <input className="input" type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required />
          <input className="input" type="password" placeholder="Mật khẩu" value={password} onChange={(e) => setPassword(e.target.value)} required />
          <button className="btn btn-primary">Đăng nhập</button>
        </form>
        {message && <p>{message}</p>}
      </div>
    </main>
  );
}
