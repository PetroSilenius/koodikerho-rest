from fastapi import FastAPI

from app.routers import product
from app.routers import shopping_list

app = FastAPI()

app.include_router(product.router)
app.include_router(shopping_list.router)
