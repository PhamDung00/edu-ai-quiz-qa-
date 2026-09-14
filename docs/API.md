# API Specification

Base URL: `/api/v1`

## Auth

### POST /auth/register

```json
{
  "email": "student@example.com",
  "password": "secret123",
  "full_name": "Nguyen Van A"
}
```

### POST /auth/login

```json
{
  "email": "student@example.com",
  "password": "secret123"
}
```

Response:

```json
{
  "access_token": "...",
  "token_type": "bearer"
}
```

## Quiz

### POST /quizzes/generate

```json
{
  "topic": "Python cơ bản",
  "difficulty": "medium",
  "question_count": 5
}
```

### POST /quizzes/{quiz_id}/submit

```json
{
  "answers": [
    {"question_id": 1, "selected_index": 2}
  ]
}
```

## Q&A

### POST /qa/ask

```json
{
  "question": "Giải thích định luật Ohm",
  "conversation_id": null
}
```
