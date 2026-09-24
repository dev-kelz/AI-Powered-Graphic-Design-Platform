from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.routes.dashboard import current_user
from app.services.asset_service import list_assets

router = APIRouter(prefix="/api/assets", tags=["assets"])


@router.get("")
def assets(request: Request, db: Session = Depends(get_db)):
    user = current_user(request, db)
    return list_assets(db, user.id if user else None)
