from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import FRONTEND_TEMPLATES
from app.database.session import get_db
from app.models.user import User
from app.services.asset_service import list_assets

router = APIRouter(prefix="/dashboard")
templates = Jinja2Templates(directory=FRONTEND_TEMPLATES)


def current_user(request: Request, db: Session) -> User | None:
    value = request.cookies.get("user_id")
    return db.get(User, int(value)) if value and value.isdigit() else None


@router.get("", response_class=HTMLResponse)
def dashboard(request: Request, db: Session = Depends(get_db)):
    user = current_user(request, db)
    if not user:
        return RedirectResponse("/auth/login", status_code=303)
    return templates.TemplateResponse(request=request, name="dashboard/index.html", context={"user": user, "assets": list_assets(db, user.id)})


@router.get("/my-assets", response_class=HTMLResponse)
def my_assets(request: Request, db: Session = Depends(get_db)):
    return dashboard(request, db)
