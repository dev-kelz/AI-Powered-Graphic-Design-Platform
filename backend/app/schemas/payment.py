from pydantic import BaseModel


class PaymentRead(BaseModel):
    id: int
    order_id: int
    amount_cents: int
    status: str
    model_config = {"from_attributes": True}
