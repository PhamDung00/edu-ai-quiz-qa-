# Project Proposal — EDU AI Quiz & Q&A

## 1. Tên đề tài

**EDU AI Quiz & Q&A — Hệ thống hỗ trợ học tập bằng trí tuệ nhân tạo, tạo câu hỏi trắc nghiệm và hỏi đáp theo nội dung học tập.**

## 2. Bối cảnh và vấn đề

Sinh viên thường mất nhiều thời gian để tự tạo câu hỏi ôn tập, kiểm tra mức độ hiểu bài và tìm lại thông tin trong tài liệu. Các công cụ hỏi đáp AI phổ thông có thể trả lời nhanh nhưng chưa gắn chặt với tiến độ học tập, lịch sử làm quiz và tài liệu của từng người dùng.

Đề tài xây dựng một nền tảng web tích hợp AI nhằm hỗ trợ người học tạo quiz theo chủ đề, làm bài và chấm điểm, theo dõi kết quả, đồng thời đặt câu hỏi cho trợ lý AI. Giai đoạn mở rộng sử dụng RAG để trả lời dựa trên tài liệu do người dùng cung cấp.

## 3. Mục tiêu

- Xây dựng ứng dụng web tách Frontend/Backend.
- Cho phép đăng ký, đăng nhập và quản lý phiên người dùng bằng JWT.
- Cho phép tạo quiz thủ công và tạo quiz tự động bằng AI.
- Cho phép làm quiz, chấm điểm, lưu lịch sử và thống kê kết quả.
- Tích hợp AI Q&A để hỗ trợ giải đáp câu hỏi học tập.
- Chuẩn bị kiến trúc PostgreSQL + pgvector cho RAG theo tài liệu.
- Có kiểm thử, CI và Docker phục vụ triển khai.

## 4. Phạm vi

### Trong phạm vi

- Web application cho sinh viên/người học.
- Authentication.
- Quiz CRUD, AI quiz generation, quiz attempt.
- AI Q&A và lưu hội thoại.
- Dashboard cơ bản.
- Upload tài liệu và vector retrieval ở giai đoạn mở rộng.

### Ngoài phạm vi phiên bản đầu

- Thi trực tuyến có giám sát chống gian lận.
- Hệ thống LMS quy mô lớn nhiều trường.
- Thanh toán học phí.
- Fine-tune mô hình AI riêng.

## 5. Đối tượng sử dụng

- **Student/User:** đăng ký, đăng nhập, tạo/làm quiz, hỏi AI, xem lịch sử và kết quả.
- **Administrator:** định hướng mở rộng để quản lý nội dung/người dùng và theo dõi hệ thống.
- **AI Service:** sinh câu hỏi và trả lời câu hỏi theo prompt/ngữ cảnh.

## 6. Công nghệ

- Frontend: Next.js, React, TypeScript.
- Backend: FastAPI, Python, SQLAlchemy.
- Database: PostgreSQL, pgvector.
- Cache: Redis.
- AI: OpenAI API.
- DevOps: Docker Compose, GitHub Actions.

## 7. Sản phẩm bàn giao

- Source code trên GitHub.
- Tài liệu khảo sát, phân tích và kiến trúc hệ thống.
- Use Case, Activity Diagram, Sequence Diagram.
- API documentation và database design.
- Sprint/Jira-ready project plan.
- Bộ kiểm thử và CI workflow.
- Bản demo chạy local bằng Docker Compose.

## 8. Tiêu chí thành công

- Người dùng đăng ký/đăng nhập được.
- AI sinh quiz hợp lệ theo chủ đề và độ khó.
- Hệ thống chấm và lưu kết quả quiz.
- Q&A trả lời được và lưu hội thoại.
- API có tài liệu Swagger.
- Code được tổ chức theo module, có test và CI.
