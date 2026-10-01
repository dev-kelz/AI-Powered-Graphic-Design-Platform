from pydantic import BaseModel


class OrderRead(BaseModel):
    id: int
    status: str
    model_config = {"from_attributes": True}
