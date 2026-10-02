from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import time
import uuid


appT = FastAPI(
    title="Learning FastAPI",
    description="This is a learning FastAPI project",
    version="1.0.0",
    contact={
        "name": "John Doe",
        "phone": 1234567890,
    }
)


# -------------------------
# Pydantic Models
# -------------------------

class Product(BaseModel):
    name: str
    price: float


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float


# -------------------------
# Timing Middleware
# -------------------------

@appT.middleware("http")
async def timing_middleware(request, call_next):

    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    duration = end_time - start_time

    print(
        f"{request.method} "
        f"{request.url.path} "
        f"completed in {duration:.4f} seconds"
    )

    return response


# -------------------------
# Request ID Middleware
# -------------------------

@appT.middleware("http")
async def request_id_middleware(request, call_next):

    request_id = str(uuid.uuid4())

    print(f"Request ID: {request_id}")

    response = await call_next(request)

    response.headers["X-Request-ID"] = request_id

    return response


# -------------------------
# Authentication Middleware
# -------------------------

@appT.middleware("http")
async def auth_middleware(request, call_next):

    # Public endpoints
    public_paths = [
        "/",
        "/docs",
        "/openapi.json",
        "/redoc"
    ]

    if request.url.path in public_paths:
        return await call_next(request)

    token = request.headers.get("Authorization")

    if token != "Bearer 123456abcd":
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"}
        )

    response = await call_next(request)

    return response


# -------------------------
# Home Endpoint
# -------------------------

@appT.get("/")
async def home():

    return {
        "message": "Welcome to learning FastAPI project"
    }


# -------------------------
# GET Products
# -------------------------

@appT.get("/products")
async def products():

    return {
        "products": [
            {
                "id": 1,
                "name": "Product 1",
                "price": 100
            },
            {
                "id": 2,
                "name": "Product 2",
                "price": 200
            },
            {
                "id": 3,
                "name": "Product 3",
                "price": 300
            }
        ]
    }


# -------------------------
# POST Product
# -------------------------

@appT.post("/products", response_model=ProductResponse)
async def create_product(product: Product):

    return {
        "id": 1,
        "name": product.name,
        "price": product.price
    }


# -------------------------
# Search Products
# -------------------------

@appT.get("/products/search")
async def search_product(limit: int = 10):

    return {
        "message": f"Searching for products with limit {limit}"
    }


# -------------------------
# Get Product by ID
# -------------------------

@appT.get("/products/{product_id}")
async def get_product(product_id: int):

    return {
        "product_id": product_id
    }