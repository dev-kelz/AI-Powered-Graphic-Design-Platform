# Backend

This folder contains the FastAPI application, its tests, configuration, and Python dependencies.

Run commands from the repository root:

```powershell
uv sync
Copy-Item backend/.env.example backend/.env
uv run uvicorn --app-dir backend app.main:app --reload
```

The application loads settings from `backend/.env`, creates the SQLite database in the repository root, and renders pages and serves static assets from `frontend/`.

Run the backend tests with `uv run pytest` from the repository root.