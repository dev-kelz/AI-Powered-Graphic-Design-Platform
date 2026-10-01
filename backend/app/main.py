from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import FRONTEND_STATIC, PROJECT_ROOT
from app.database.base import Base
from app.database.connection import engine
from app.models import Asset, Order, Payment, User
from app.routes import ai, assets, auth, dashboard, home, marketplace, payments

Base.metadata.create_all(bind=engine)
(PROJECT_ROOT / "uploads").mkdir(exist_ok=True)

app = FastAPI(title="Kelz Graphics Studio", version="0.1.0")
app.mount("/static", StaticFiles(directory=FRONTEND_STATIC), name="static")
app.include_router(home.router)
app.include_router(auth.router)
app.include_router(dashboard.router)
app.include_router(ai.router)
app.include_router(assets.router)
app.include_router(marketplace.router)
app.include_router(payments.router)


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}
