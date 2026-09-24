from sqlalchemy.orm import Session

from app.models.order import Order
from app.models.payment import Payment


def create_order(db: Session, user_id: int, amount_cents: int) -> Order:
    order = Order(user_id=user_id)
    db.add(order)
    db.flush()
    db.add(Payment(order_id=order.id, amount_cents=amount_cents))
    db.commit()
    db.refresh(order)
    return order
