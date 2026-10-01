from pydantic import BaseModel, Field


class AssetCreate(BaseModel):
    title: str = Field(min_length=1, max_length=180)
    prompt: str | None = None


class AssetRead(BaseModel):
    id: int
    title: str
    prompt: str | None
    image_url: str | None

    model_config = {"from_attributes": True}
