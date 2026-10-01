from fastapi import FastAPI
from pydantic import BaseModel
import time

appT = FastAPI(
    title = "learning fastapi",
    description = "This is a learning fastapi project",
    version = "1.0.0",
    contact = {
        "name": "John Doe",
        "phone" : 1234567890,
    }
)


@appT.get("/")
async def home():
    return {
        "Message" : "Welcome to learning fastapi project"
    }

@appT.get("/products")
async def products():
    return {
        "products" :[
                {
                    "id" : 1,
                    "name" : "Product 1",
                    "price" : 100
                },
                {
                    "id" : 2,
                    "name" : "Product 2",
                    "price" : 200
                },
                {
                    "id" : 3,
                    "name" : "Product 3",
                    "price" : 300
                }


        ]
    }

@appT.post("/products")
async def create_product(product: dict):
    return {
        "message" : "Product created successfully",
        "product" : product
    }


@appT.get("/products/search")
async def search_product(limit:int=10):
    return {
        "message" : f"Searching for products with limit {limit}"
    }


@appT.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time()
    duration = end_time - start_time
    print(f"{request.method} {request.url.path} completed in {duration:.4f} seconds")
    return response

import uuid

@appT.middleware("http")
async def request_id_middleware(request, call_next):
    request_id = str(uuid.uuid4())
    print(f"Request ID: {request_id}")
    response = await call_next(request)
    # response.headers["X-Request-ID"] = request_id
    return response


from fastapi.responses import JSONResponse

@appT.middleware("http")
async def auth_middleware(request, call_next):

    # Allow the home endpoint without authentication
    if request.url.path == "/":
        return await call_next(request)

    token = request.headers.get("Authorization")

    if token != "Bearer my-secret-token":
        return JSONResponse(
            status_code=401,
            content={"detail": "Unauthorized"}
        )

    response = await call_next(request)

    return response








