"""Health check router."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check() -> dict:
    """Return the health status of the API.

    Returns:
        dict: A dictionary with key 'status' set to 'ok'.
    """
    return {"status": "ok"}
