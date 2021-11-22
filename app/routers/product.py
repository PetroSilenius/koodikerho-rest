from fastapi import APIRouter

from app.db import data
from app.db.queries import (
    get_list_by_id,
    get_product_from_list_by_id,
    update_product_from_list_by_id,
)
from app.models import Product

router = APIRouter()

@router.get("/lists/{list_id}/products", response_model=list[Product])
def get_products(list_id: int) -> list[Product]:
    return get_list_by_id(list_id).products

@router.get("/lists/{list_id}/products/{product_id}", response_model=Product)
def get_product(list_id: int, product_id: int) -> Product:
    return get_product_from_list_by_id(list_id, product_id)

@router.put("/lists/{list_id}/products/{product_id}", response_model=Product)
def update_product(list_id: int, product_id: int, product: Product) -> Product:
    return update_product_from_list_by_id(list_id, product_id, product)
