# EDU AI Quiz & Q&A

Nền tảng học tập sử dụng AI để tạo quiz tự động, chấm điểm, theo dõi tiến độ và hỏi đáp theo ngữ cảnh tài liệu học tập.

## Tính năng chính

- Đăng ký / đăng nhập bằng JWT.
- Tạo quiz thủ công hoặc sinh quiz bằng AI theo chủ đề.
- Làm bài, chấm điểm và lưu lịch sử kết quả.
- Q&A với AI theo ngữ cảnh học tập.
- Kiến trúc sẵn sàng mở rộng RAG với PostgreSQL + pgvector.
- Dashboard theo dõi quiz, điểm số và hoạt động gần đây.
- Docker Compose cho môi trường phát triển.
- GitHub Actions kiểm tra backend/frontend.

## Kiến trúc

```text
Browser
  |
  v
Next.js Frontend  --->  FastAPI Backend  ---> PostgreSQL + pgvector
                              |                     |
                              |                     +--> Quiz/User/Attempt data
                              |
                              +--> OpenAI API
                              +--> Redis cache
```

## Cấu trúc thư mục

```text
edu-ai-quiz-qa/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── workflows/ci.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── backend/
│   ├── app/
│   │   ├── api/v1/routes/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── tests/
│   ├── Dockerfile
│   └── pyproject.toml
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── Dockerfile
│   └── package.json
├── docs/
├── scripts/
├── .env.example
├── docker-compose.yml
└── Makefile
```

## Chạy nhanh bằng Docker

1. Sao chép biến môi trường:

```bash
cp .env.example .env
```

2. Điền `OPENAI_API_KEY` trong `.env`.

3. Khởi động:

```bash
docker compose up --build
```

4. Truy cập:

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Swagger: http://localhost:8000/docs

## Chạy local không Docker

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## API chính

| Method | Endpoint | Mô tả |
|---|---|---|
| GET | `/api/v1/health` | Health check |
| POST | `/api/v1/auth/register` | Đăng ký |
| POST | `/api/v1/auth/login` | Đăng nhập |
| POST | `/api/v1/quizzes/generate` | Sinh quiz bằng AI |
| GET | `/api/v1/quizzes` | Danh sách quiz |
| GET | `/api/v1/quizzes/{id}` | Chi tiết quiz |
| POST | `/api/v1/quizzes/{id}/submit` | Nộp bài |
| POST | `/api/v1/qa/ask` | Hỏi AI |

## Roadmap

- [x] Khung monorepo frontend/backend.
- [x] Auth JWT cơ bản.
- [x] Quiz generation service.
- [x] Q&A service.
- [x] Database models.
- [x] Docker Compose + CI.
- [ ] Upload PDF/DOCX và chunk tài liệu.
- [ ] Embedding + semantic search bằng pgvector.
- [ ] Admin panel quản lý người dùng/câu hỏi.
- [ ] Phân tích năng lực học tập theo chủ đề.
- [ ] Gamification, leaderboard, badge.

## Công nghệ

- Frontend: Next.js 16, React 19, TypeScript.
- Backend: FastAPI, SQLAlchemy async, Pydantic.
- Database: PostgreSQL + pgvector.
- Cache: Redis.
- AI: OpenAI API.
- DevOps: Docker Compose, GitHub Actions.

## Quy ước nhánh

- `main`: ổn định.
- `develop`: tích hợp.
- `feature/*`: tính năng mới.
- `fix/*`: sửa lỗi.

## License

MIT.
