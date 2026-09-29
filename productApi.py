from fastapi import APIRouter, FastAPI

app = FastAPI(
    title="Product API",
    description="An API for managing products",
    version="1.0.0",
)

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
async def get_products():
    return {
        "usage":[
            {"/products": "Get all products"},
            {"/products/<pid>": "Get a product by ID"},
            {"/products/insert": "Insert a new product"},
        ]
    }

@router.get("/list")
async def list_products():
    return {
        "products": [
            {"id": 1, "name": "Product A", "price": 10.99},
            {"id": 2, "name": "Product B", "price": 19.99},
            {"id": 3, "name": "Product C", "price": 5.49},
        ]
    }

@router.get("/{pid}")
async def get_product(pid: int):
    products = {
        1: {"id": 1, "name": "Product A", "price": 10.99},
        2: {"id": 2, "name": "Product B", "price": 19.99},
        3: {"id": 3, "name": "Product C", "price": 5.49},
    }
    product = products.get(pid)
    if product:
        return product
    return {"error": "Product not found"}

@router.post("/insert")
async def insert_product(product: dict):
    return{
"message": "Product inserted successfully", "product": product
    }

app.include_router(router)

