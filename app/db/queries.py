from fastapi import HTTPException
from app.db import data
from app.models import ShoppingList

def get_list_by_id(list_id: int) -> ShoppingList:
    for shopping_list in data["lists"]:
        if shopping_list["id"] == list_id:
            return ShoppingList.parse_obj(shopping_list)
    raise HTTPException(status_code=404, detail="Shopping list not found")
