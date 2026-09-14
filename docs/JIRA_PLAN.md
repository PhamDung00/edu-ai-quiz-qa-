# Jira-ready Project Plan — EDU AI Quiz & Q&A

## 1. Cấu hình Jira đề xuất

**Project name:** EDU AI Quiz & Q&A  
**Project key:** EDUAI  
**Method:** Scrum  
**Sprint length:** 1 week  
**Estimation:** Story Points (Fibonacci: 1, 2, 3, 5, 8, 13)

### Issue types

- Epic
- Story
- Task
- Bug
- Spike

### Workflow

`Backlog -> Selected for Development -> In Progress -> Code Review -> Testing -> Done`

### Definition of Ready

Một ticket được đưa vào Sprint khi:

- Mục tiêu rõ ràng.
- Có acceptance criteria.
- Đã xác định dependency chính.
- Có estimate story points.
- Có người phụ trách.

### Definition of Done

Một ticket được coi là Done khi:

- Code hoàn thành.
- Không chứa secret/API key trong source.
- Code đã review.
- Test liên quan pass.
- CI pass.
- Tài liệu/API được cập nhật nếu có thay đổi.
- Acceptance criteria được đáp ứng.

---

## 2. Epics

| Epic | Nội dung |
|---|---|
| EPIC-01 Foundation & DevOps | Repo, cấu trúc, Docker, CI, database |
| EPIC-02 Authentication | User, password hashing, JWT, login UI |
| EPIC-03 Quiz Core | Quiz CRUD, questions, attempt, scoring |
| EPIC-04 AI Quiz Generation | Prompt, structured output, validation |
| EPIC-05 AI Q&A | Chat, conversations, AI response |
| EPIC-06 RAG Documents | Upload, parsing, embedding, retrieval |
| EPIC-07 Dashboard & Analytics | History, scores, progress analytics |
| EPIC-08 Quality & Release | Test, security, performance, deployment docs |

---

## 3. Sprint 1 — Foundation & DevOps

**Sprint Goal:** Tạo nền tảng kỹ thuật có thể chạy local và CI.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-1 | Story | Khởi tạo monorepo frontend/backend | 3 | Highest |
| EDUAI-2 | Task | Thiết lập FastAPI và health endpoint | 2 | High |
| EDUAI-3 | Task | Thiết lập Next.js application shell | 3 | High |
| EDUAI-4 | Task | PostgreSQL + Redis + Docker Compose | 5 | Highest |
| EDUAI-5 | Task | Thiết lập environment configuration | 2 | High |
| EDUAI-6 | Task | GitHub Actions CI | 3 | High |

**Total:** 18 SP

### Acceptance Criteria

- `docker compose up --build` khởi động được các service chính.
- Backend có health endpoint.
- Frontend chạy được.
- CI được trigger khi push/PR.

---

## 4. Sprint 2 — Authentication

**Sprint Goal:** Người dùng có thể đăng ký, đăng nhập và truy cập API được bảo vệ.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-7 | Story | User model và migration | 3 | Highest |
| EDUAI-8 | Story | Register API | 3 | Highest |
| EDUAI-9 | Story | Login API + JWT | 5 | Highest |
| EDUAI-10 | Task | Password hashing/security helpers | 3 | Highest |
| EDUAI-11 | Story | Login/Register UI | 5 | High |
| EDUAI-12 | Task | Authentication tests | 3 | High |

**Total:** 22 SP

### Acceptance Criteria

- Email trùng không đăng ký được.
- Password được hash.
- Login đúng trả JWT.
- Endpoint yêu cầu auth từ chối token không hợp lệ.

---

## 5. Sprint 3 — Quiz Core

**Sprint Goal:** Hoàn thiện nghiệp vụ quiz không phụ thuộc AI.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-13 | Story | Quiz/Question data models | 5 | Highest |
| EDUAI-14 | Story | Quiz CRUD API | 5 | Highest |
| EDUAI-15 | Story | Quiz detail UI | 3 | High |
| EDUAI-16 | Story | Take Quiz UI | 5 | Highest |
| EDUAI-17 | Story | Submit, scoring và feedback | 5 | Highest |
| EDUAI-18 | Story | Attempt/history persistence | 5 | High |

**Total:** 28 SP

---

## 6. Sprint 4 — AI Quiz Generator

**Sprint Goal:** Sinh quiz tự động có cấu trúc và kiểm soát lỗi.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-19 | Spike | Thiết kế prompt và schema AI output | 3 | Highest |
| EDUAI-20 | Story | OpenAI integration service | 5 | Highest |
| EDUAI-21 | Story | Generate quiz endpoint | 5 | Highest |
| EDUAI-22 | Task | Validate structured output | 3 | Highest |
| EDUAI-23 | Task | Retry/error handling | 3 | High |
| EDUAI-24 | Story | AI Quiz Generator UI | 5 | High |

**Total:** 24 SP

### Acceptance Criteria

- User chọn topic, difficulty, question count.
- AI output được validate trước khi lưu.
- Không lưu quiz malformed.
- Lỗi AI được trả về frontend có kiểm soát.

---

## 7. Sprint 5 — AI Q&A

**Sprint Goal:** Người dùng có thể chat với trợ lý AI và lưu lịch sử.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-25 | Story | Conversation/Message models | 3 | High |
| EDUAI-26 | Story | Q&A API | 5 | Highest |
| EDUAI-27 | Story | Chat UI | 5 | Highest |
| EDUAI-28 | Story | Persist conversation history | 5 | High |
| EDUAI-29 | Task | Conversation context management | 3 | High |
| EDUAI-30 | Task | AI Q&A error handling/tests | 3 | High |

**Total:** 24 SP

---

## 8. Sprint 6 — RAG Documents

**Sprint Goal:** Q&A có thể sử dụng tài liệu học tập của người dùng làm nguồn context.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-31 | Story | Document upload endpoint | 5 | High |
| EDUAI-32 | Task | Parse and chunk documents | 5 | High |
| EDUAI-33 | Task | Generate embeddings | 5 | High |
| EDUAI-34 | Story | pgvector similarity retrieval | 8 | Highest |
| EDUAI-35 | Story | RAG prompt pipeline | 8 | Highest |
| EDUAI-36 | Story | Document management UI | 5 | Medium |

**Total:** 36 SP

---

## 9. Sprint 7 — Dashboard & Analytics

**Sprint Goal:** Hiển thị tiến độ học tập và kết quả cho người dùng.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-37 | Story | Dashboard overview | 5 | High |
| EDUAI-38 | Story | Quiz attempt history | 3 | High |
| EDUAI-39 | Story | Average score/statistics | 5 | High |
| EDUAI-40 | Story | Topic strength/weakness analysis | 5 | Medium |
| EDUAI-41 | Story | Progress charts | 5 | Medium |

**Total:** 23 SP

---

## 10. Sprint 8 — Stabilization & Release

**Sprint Goal:** Chuẩn hóa sản phẩm để demo/nộp đồ án.

| Key | Type | Task | SP | Priority |
|---|---|---|---:|---|
| EDUAI-42 | Task | Backend unit/integration tests | 5 | Highest |
| EDUAI-43 | Task | Frontend lint/build verification | 3 | High |
| EDUAI-44 | Task | Security review | 5 | Highest |
| EDUAI-45 | Task | Performance review | 3 | Medium |
| EDUAI-46 | Task | Demo seed/sample data | 3 | Medium |
| EDUAI-47 | Task | Final documentation | 5 | High |
| EDUAI-48 | Task | Deployment guide | 3 | High |

**Total:** 27 SP

---

## 11. Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| AI output sai schema | Medium | High | Structured output + validation + retry |
| AI API unavailable/rate limited | Medium | High | Graceful error, retry, cache where appropriate |
| API key bị commit | Low | Critical | `.env`, `.gitignore`, secret review |
| RAG retrieval kém chính xác | Medium | Medium | Chunking experiment, top-k tuning, metadata |
| Scope quá lớn | High | High | Ưu tiên Must-have trước, RAG/analytics mở rộng sau |
| Thiếu test trước demo | Medium | High | CI từ đầu, test theo từng Sprint |

---

## 12. Traceability

- Project proposal: `docs/PROJECT_PROPOSAL.md`
- System analysis: `docs/SYSTEM_ANALYSIS.md`
- Architecture: `docs/ARCHITECTURE.md`
- API: `docs/API.md`
- Database: `docs/DATABASE.md`
- Sprint plan: `docs/SPRINT_PLAN.md`
- Jira-ready plan: `docs/JIRA_PLAN.md`
