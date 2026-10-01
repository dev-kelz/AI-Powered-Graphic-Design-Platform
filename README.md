# Kelz Graphics Studio

A FastAPI starter for an AI-powered graphic design platform. It includes a local SQLite database, SQLAlchemy models, cookie-based starter authentication, Jinja templates, asset storage records, and placeholder boundaries for AI generation, Cloudinary, and payments.

## Run locally

Requires Python 3.11 or newer.

```powershell
uv sync
Copy-Item backend/.env.example backend/.env
uv run uvicorn --app-dir backend app.main:app --reload
```

Open http://127.0.0.1:8000. API documentation is available at http://127.0.0.1:8000/docs.

## Project notes

- `backend/app/main.py` creates the local SQLite tables on startup. Use Alembic migrations before production.
- The FastAPI backend renders templates and serves assets from `frontend/`; the folders are separated, but the frontend is not yet an independently deployed application.
- AI generation currently saves the prompt and creates an asset record; connect the provider in `backend/app/ai/` next.
- Payment and Cloudinary integrations are intentionally placeholders until provider credentials are configured.
- Set a strong `SECRET_KEY` and move from the starter cookie auth to signed/session-backed auth before deploying publicly.

## Checks

```powershell
uv run python -m compileall backend/app
uv run pytest
```
