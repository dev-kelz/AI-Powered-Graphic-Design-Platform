from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import FRONTEND_TEMPLATES
from app.database.session import get_db
from app.models.asset import Asset
from app.routes.dashboard import current_user
from app.services.asset_service import create_asset

router = APIRouter(prefix="/ai")
templates = Jinja2Templates(directory=FRONTEND_TEMPLATES)


@router.get("/generator", response_class=HTMLResponse)
def generator(request: Request):
    return templates.TemplateResponse(request=request, name="ai/generator.html")


@router.post("/generate")
def generate(request: Request, prompt: str = Form(...), db: Session = Depends(get_db)):
    user = current_user(request, db)
    if not user:
        return RedirectResponse("/auth/login", status_code=303)
    asset = create_asset(db, user.id, title=prompt[:60], prompt=prompt)
    return RedirectResponse(f"/ai/result/{asset.id}", status_code=303)


@router.get("/result/{asset_id}", response_class=HTMLResponse)
def result(request: Request, asset_id: int, db: Session = Depends(get_db)):
    user = current_user(request, db)
    asset = db.get(Asset, asset_id)
    return templates.TemplateResponse(request=request, name="ai/result.html", context={"asset": asset, "user": user})
