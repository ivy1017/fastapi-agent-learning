from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.order import DouplusOrder

router = APIRouter()


@router.get("/orders/{user_id}")
def get_order(user_id: str):
    db: Session = SessionLocal()

    order = (
        db.query(DouplusOrder)
        .filter(DouplusOrder.user_id == user_id)
        .first()
    )

    db.close()

    if not order:
        return {"error": "order not found"}

    return {
        "user_id": order.user_id,
        "budget": order.budget,
        "roi": order.roi,
        "ctr": order.ctr,
        "cpm": order.cpm
    }