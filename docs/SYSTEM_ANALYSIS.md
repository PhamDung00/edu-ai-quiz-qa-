# System Analysis — EDU AI Quiz & Q&A

## 1. Use Case Diagram

```mermaid
flowchart LR
    U[Student / User]
    A[Administrator]
    AI[AI Service]

    UC1((Register / Login))
    UC2((Manage Profile))
    UC3((Create Quiz))
    UC4((Generate Quiz with AI))
    UC5((Take Quiz))
    UC6((Submit & View Score))
    UC7((View Quiz History))
    UC8((Ask AI))
    UC9((View Conversation History))
    UC10((Upload Learning Document))
    UC11((Answer from Documents / RAG))
    UC12((View Dashboard))
    UC13((Manage Users / Content))

    U --> UC1
    U --> UC2
    U --> UC3
    U --> UC4
    U --> UC5
    U --> UC6
    U --> UC7
    U --> UC8
    U --> UC9
    U --> UC10
    U --> UC11
    U --> UC12

    A --> UC13

    UC4 --> AI
    UC8 --> AI
    UC11 --> AI
```

## 2. Use Case Description

### UC-01 — Register / Login

**Actor:** User  
**Precondition:** User chưa đăng nhập.  
**Main flow:**
1. User nhập thông tin đăng ký hoặc tài khoản đăng nhập.
2. Frontend gửi request tới backend.
3. Backend kiểm tra dữ liệu và mật khẩu.
4. Backend trả JWT nếu hợp lệ.
5. Frontend lưu trạng thái đăng nhập và chuyển tới dashboard.

**Postcondition:** User có phiên đăng nhập hợp lệ.

### UC-02 — Generate Quiz with AI

**Actor:** User, AI Service  
**Precondition:** User đã đăng nhập.  
**Main flow:**
1. User nhập chủ đề, độ khó, số câu hỏi.
2. Backend xây dựng prompt.
3. AI Service sinh dữ liệu quiz dạng structured output.
4. Backend validate kết quả.
5. Quiz và câu hỏi được lưu vào database.
6. Quiz được trả về frontend.

**Alternative flow:** AI trả dữ liệu sai định dạng → backend retry hoặc trả lỗi có kiểm soát.

### UC-03 — Take Quiz & Submit

**Actor:** User  
**Precondition:** Quiz tồn tại.  
**Main flow:**
1. User mở quiz.
2. Hệ thống hiển thị câu hỏi và đáp án.
3. User chọn đáp án.
4. User submit bài.
5. Backend chấm điểm.
6. Backend lưu attempt.
7. Frontend hiển thị điểm và feedback.

### UC-04 — Ask AI

**Actor:** User, AI Service  
**Precondition:** User đã đăng nhập.  
**Main flow:**
1. User nhập câu hỏi.
2. Backend lấy lịch sử hội thoại và/hoặc context tài liệu.
3. Backend gửi prompt đến AI Service.
4. AI trả câu trả lời.
5. Hệ thống lưu message và response.
6. Frontend hiển thị câu trả lời.

## 3. Activity Diagram — AI Quiz Generation

```mermaid
flowchart TD
    S([Start]) --> A[User enters topic, difficulty, question count]
    A --> B{Authenticated?}
    B -- No --> C[Redirect to Login]
    C --> E([End])
    B -- Yes --> D[POST /api/v1/quizzes/generate]
    D --> F[Validate request]
    F --> G{Valid?}
    G -- No --> H[Return validation error]
    H --> E
    G -- Yes --> I[Build AI prompt]
    I --> J[Call AI service]
    J --> K{Valid structured output?}
    K -- No --> L[Retry / controlled error]
    L --> E
    K -- Yes --> M[Save quiz and questions]
    M --> N[Return quiz]
    N --> O[Display generated quiz]
    O --> E
```

## 4. Activity Diagram — Q&A

```mermaid
flowchart TD
    S([Start]) --> A[User enters question]
    A --> B[Send question to backend]
    B --> C[Load conversation history]
    C --> D{Document context enabled?}
    D -- Yes --> E[Retrieve relevant chunks from pgvector]
    D -- No --> F[Build prompt without document context]
    E --> G[Build prompt with retrieved context]
    F --> H[Call AI]
    G --> H
    H --> I[Receive answer]
    I --> J[Save user message and AI response]
    J --> K[Display answer]
    K --> L([End])
```

## 5. Sequence Diagram — Authentication

```mermaid
sequenceDiagram
    actor U as User
    participant F as Frontend
    participant B as FastAPI Backend
    participant DB as PostgreSQL

    U->>F: Enter email/password
    F->>B: POST /auth/login
    B->>DB: Find user by email
    DB-->>B: User record
    B->>B: Verify password
    B-->>F: JWT access token
    F-->>U: Redirect to dashboard
```

## 6. Sequence Diagram — AI Quiz

```mermaid
sequenceDiagram
    actor U as User
    participant F as Frontend
    participant B as Backend
    participant AI as OpenAI API
    participant DB as PostgreSQL

    U->>F: Enter topic/difficulty/count
    F->>B: POST /quizzes/generate
    B->>AI: Structured quiz prompt
    AI-->>B: Quiz JSON
    B->>B: Validate response
    B->>DB: Save quiz + questions
    DB-->>B: Quiz ID
    B-->>F: Generated quiz
    F-->>U: Display quiz
```

## 7. Sequence Diagram — Quiz Submission

```mermaid
sequenceDiagram
    actor U as User
    participant F as Frontend
    participant B as Backend
    participant DB as PostgreSQL

    U->>F: Select answers
    U->>F: Submit
    F->>B: POST /quizzes/{id}/submit
    B->>DB: Load questions/correct answers
    DB-->>B: Quiz data
    B->>B: Calculate score
    B->>DB: Save attempt
    DB-->>B: Attempt ID
    B-->>F: Score + feedback
    F-->>U: Show result
```

## 8. Sequence Diagram — AI Q&A with RAG

```mermaid
sequenceDiagram
    actor U as User
    participant F as Frontend
    participant B as Backend
    participant V as pgvector
    participant AI as OpenAI API
    participant DB as PostgreSQL

    U->>F: Ask question
    F->>B: POST /qa/ask
    B->>V: Similarity search
    V-->>B: Relevant chunks
    B->>AI: Question + context + history
    AI-->>B: Answer
    B->>DB: Save conversation/messages
    DB-->>B: Saved
    B-->>F: Answer
    F-->>U: Display answer
```

## 9. Main Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-01 | User can register and login | Must |
| FR-02 | User can create and view quizzes | Must |
| FR-03 | AI can generate quizzes | Must |
| FR-04 | User can take and submit quizzes | Must |
| FR-05 | System saves score/history | Must |
| FR-06 | User can ask AI questions | Must |
| FR-07 | System stores conversations | Should |
| FR-08 | User can upload documents | Should |
| FR-09 | Q&A can retrieve document context | Should |
| FR-10 | Dashboard shows learning progress | Should |

## 10. Non-functional Requirements

- **Security:** password hashing, JWT authentication, secrets stored in environment variables.
- **Performance:** common API response target under 2 seconds excluding AI latency.
- **Maintainability:** frontend/backend separation, service layer, schemas and models separated.
- **Scalability:** PostgreSQL, Redis and stateless API architecture.
- **Reliability:** input validation, controlled AI errors, tests and CI.
- **Usability:** responsive web interface and simple learning flow.
