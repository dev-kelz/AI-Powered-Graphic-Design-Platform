from fastapi import APIRouter

router = APIRouter(prefix="/api/payments", tags=["payments"])


@router.get("/health")
def payment_health():
    return {"status": "ready", "provider": "local-placeholder"}
