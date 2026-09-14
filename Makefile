.PHONY: up down logs backend-test backend-lint frontend-lint format

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

backend-test:
	cd backend && pytest

backend-lint:
	cd backend && ruff check .

frontend-lint:
	cd frontend && npm run lint

format:
	cd backend && ruff format .
