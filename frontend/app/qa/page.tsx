"use client";

import { FormEvent, useState } from "react";
import { askAI } from "@/lib/api";

type Message = { role: "user" | "assistant"; content: string };

export default function QAPage() {
  const [question, setQuestion] = useState("");
  const [conversationId, setConversationId] = useState<number | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  async function submit(event: FormEvent) {
    event.preventDefault();
    const text = question.trim();
    if (!text || loading) return;

    setQuestion("");
    setMessages((prev) => [...prev, { role: "user", content: text }]);
    setLoading(true);
    try {
      const data = await askAI(text, conversationId);
      setConversationId(data.conversation_id);
      setMessages((prev) => [...prev, { role: "assistant", content: data.answer }]);
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="section container">
      <h1>AI Q&A</h1>
      <p className="muted">Hỏi kiến thức và nhận giải thích từ trợ giảng AI.</p>
      <div className="chat">
        {messages.length === 0 && <div className="card">Ví dụ: “Giải thích định luật Ohm theo cách dễ hiểu.”</div>}
        {messages.map((message, i) => (
          <div key={i} className={`message ${message.role}`}>{message.content}</div>
        ))}
      </div>
      <form className="form" onSubmit={submit}>
        <textarea className="input" rows={4} value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Nhập câu hỏi..." />
        <button className="btn btn-primary" disabled={loading}>{loading ? "AI đang trả lời..." : "Gửi câu hỏi"}</button>
      </form>
    </main>
  );
}
