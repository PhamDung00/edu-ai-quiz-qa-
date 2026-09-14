# Database Design

## users

- id
- email
- hashed_password
- full_name
- role
- created_at

## quizzes

- id
- title
- topic
- difficulty
- owner_id
- created_at

## questions

- id
- quiz_id
- content
- options (JSON)
- correct_index
- explanation

## attempts

- id
- quiz_id
- user_id
- score
- total_questions
- answers (JSON)
- submitted_at

## conversations

- id
- user_id
- title
- created_at

## messages

- id
- conversation_id
- role
- content
- created_at

## documents

- id
- owner_id
- file_name
- status
- created_at

Phase 2 sẽ bổ sung `document_chunks` với cột embedding `vector` từ pgvector.
