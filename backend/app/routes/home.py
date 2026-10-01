from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.config import FRONTEND_TEMPLATES

router = APIRouter()
templates = Jinja2Templates(directory=FRONTEND_TEMPLATES)


@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="home/index.html")
