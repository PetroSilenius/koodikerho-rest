from fastapi import APIRouter

from app.db import data
from app.models import ShoppingList

router = APIRouter()

@router.get("/lists", response_model=list[ShoppingList])
def get_lists() -> list[ShoppingList]:
    return data["lists"]
