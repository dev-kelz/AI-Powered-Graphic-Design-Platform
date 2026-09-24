from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.asset import Asset


def list_assets(db: Session, owner_id: int | None = None) -> list[Asset]:
    statement = select(Asset).order_by(Asset.created_at.desc())
    if owner_id is not None:
        statement = statement.where(Asset.owner_id == owner_id)
    return list(db.scalars(statement))


def create_asset(db: Session, owner_id: int, title: str, prompt: str | None = None) -> Asset:
    asset = Asset(owner_id=owner_id, title=title, prompt=prompt)
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset
