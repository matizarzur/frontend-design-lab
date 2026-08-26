from fastapi import APIRouter, HTTPException, Query

from ..data import PRODUCTS, USERS
from ..models import Product, User

router = APIRouter(tags=["mock data"])


@router.get("/users", response_model=list[User])
def list_users(limit: int = Query(default=20, ge=1, le=100), offset: int = 0):
    return USERS[offset : offset + limit]


@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in USERS:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/products", response_model=list[Product])
def list_products(limit: int = Query(default=20, ge=1, le=100), offset: int = 0):
    return PRODUCTS[offset : offset + limit]


@router.get("/products/{product_id}", response_model=Product)
def get_product(product_id: int):
    for product in PRODUCTS:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")
