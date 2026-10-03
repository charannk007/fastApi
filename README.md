# Learning FastAPI

A learning project for building a **modular FastAPI backend with PostgreSQL**.

This repository is being used to learn and build backend architecture step by step, starting with a Product CRUD API and later extending it with middleware, authentication, streaming, LLM integration, and Agentic AI concepts.

---

## Project Goals

This project covers:

- FastAPI fundamentals
- API and REST API concepts
- Project modularization
- Python packages
- FastAPI routers
- Pydantic request/response validation
- Swagger / OpenAPI documentation
- PostgreSQL integration
- Async PostgreSQL using `asyncpg`
- Service-layer architecture
- CRUD operations
- Middleware
- Authentication
- Server-Sent Events (SSE)
- `StreamingResponse`
- LLM response streaming
- Agentic AI backend architecture

---

## Project Structure

```text
FastAPi/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   └── config.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── product.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   └── products.py
│   │
│   └── services/
│       ├── __init__.py
│       └── product_service.py
│
├── oldapi/
│   ├── database.py
│   ├── productApi.py
│   ├── learning.py
│   └── timeauth.py
│
├── .env
├── .gitignore
└── README.md
```

---

## Architecture

The application follows a layered architecture:

```text
Client
  │
  ▼
FastAPI
  │
  ▼
Router
  │
  ▼
Pydantic Schema
  │
  ▼
Service Layer
  │
  ▼
Database Connection
  │
  ▼
PostgreSQL
```

### Responsibilities

#### `main.py`

Creates and configures the FastAPI application.

```text
app/main.py
```

#### `routers/`

Contains API endpoints.

```text
app/routers/products.py
```

Responsible for handling HTTP requests and responses.

#### `schemas/`

Contains Pydantic models used for API validation.

```text
app/schemas/product.py
```

Example:

```python
class ProductCreate(BaseModel):
    name: str
    price: float
```

#### `services/`

Contains business logic.

```text
app/services/product_service.py
```

The router should not contain database logic. It calls the service layer.

#### `database/`

Contains PostgreSQL connection logic.

```text
app/database/connection.py
```

Uses `asyncpg`.

#### `models/`

Contains database-related models/table definitions.

```text
app/models/product.py
```

---

## Technologies

- Python
- FastAPI
- Pydantic
- PostgreSQL
- asyncpg
- python-dotenv
- Uvicorn
- Swagger / OpenAPI

---

## Environment Setup

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=nkcharan
DB_PASSWORD=your_password
```

Do not commit `.env` to Git.

Example `.gitignore`:

```gitignore
.env

__pycache__/
*.py[cod]

.venv/
```

---

## Install Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn asyncpg python-dotenv
```

---

## PostgreSQL

The project uses PostgreSQL as its database.

The current database contains a `products` table:

```sql
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price FLOAT NOT NULL
);
```

Check the table:

```sql
SELECT * FROM products;
```

---

## Running the Application

From the project root:

```bash
uvicorn app.main:app --reload
```

The application runs at:

```text
http://127.0.0.1:8000
```

---

## Swagger Documentation

FastAPI automatically generates interactive API documentation.

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger can be used to test the API without Postman.

OpenAPI JSON is available at:

```text
http://127.0.0.1:8000/openapi.json
```

---

# Product API

## Create Product

### Endpoint

```http
POST /products/
```

### Request

```json
{
    "name": "Laptop",
    "price": 50000
}
```

### Response

```json
{
    "id": 1,
    "name": "Laptop",
    "price": 50000
}
```

---

## Get All Products

### Endpoint

```http
GET /products/
```

### Response

```json
[
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000
    }
]
```

---

## Get Product by ID

### Endpoint

```http
GET /products/{product_id}
```

Example:

```http
GET /products/1
```

Response:

```json
{
    "id": 1,
    "name": "Laptop",
    "price": 50000
}
```

If the product doesn't exist:

```json
{
    "detail": "Product not found"
}
```

HTTP status:

```text
404 Not Found
```

---

## Update Product

### Endpoint

```http
PUT /products/{product_id}
```

Example:

```http
PUT /products/1
```

Request:

```json
{
    "name": "MacBook",
    "price": 75000
}
```

Response:

```json
{
    "id": 1,
    "name": "MacBook",
    "price": 75000
}
```

---

## Delete Product

### Endpoint

```http
DELETE /products/{product_id}
```

Example:

```http
DELETE /products/1
```

Response:

```json
{
    "message": "Product deleted successfully",
    "product_id": 1
}
```

---

# CRUD Flow

The Product API implements complete CRUD:

```text
CREATE
POST /products/
        ↓
     INSERT
        ↓
   PostgreSQL


READ ALL
GET /products/
        ↓
      SELECT
        ↓
   PostgreSQL


READ ONE
GET /products/{id}
        ↓
   SELECT WHERE id
        ↓
   PostgreSQL


UPDATE
PUT /products/{id}
        ↓
      UPDATE
        ↓
   PostgreSQL


DELETE
DELETE /products/{id}
        ↓
      DELETE
        ↓
   PostgreSQL
```

---

# Request Flow

For example, when creating a product:

```text
POST /products/
       │
       ▼
products.py
(Router)
       │
       ▼
ProductCreate
(Pydantic)
       │
       ▼
product_service.py
       │
       ▼
get_db_connection()
       │
       ▼
asyncpg
       │
       ▼
PostgreSQL
       │
       ▼
ProductResponse
       │
       ▼
Client
```

---

# Learning Progress

### Completed

- [x] FastAPI application
- [x] Python package structure
- [x] FastAPI routers
- [x] Pydantic schemas
- [x] PostgreSQL connection
- [x] PostgreSQL products table
- [x] Service layer
- [x] Create product
- [x] Get all products
- [x] Get product by ID
- [x] Update product
- [x] Delete product
- [x] Swagger / OpenAPI

### Planned

- [ ] Configuration management
- [ ] Database connection lifecycle
- [ ] Middleware
- [ ] Request ID
- [ ] Timing middleware
- [ ] Authentication
- [ ] Error handling
- [ ] Pagination
- [ ] Dependency injection
- [ ] SSE
- [ ] StreamingResponse
- [ ] OpenAI streaming
- [ ] Agentic AI backend
- [ ] Scalable backend architecture

---

# Purpose of `oldapi`

The `oldapi/` directory contains earlier versions of the learning code.

It is kept for reference while the project is being converted into a modular architecture.

```text
oldapi/
├── database.py
├── productApi.py
├── learning.py
└── timeauth.py
```

The new implementation lives under:

```text
app/
```

---

# Future Projects

This repository will also be used as the foundation for additional backend projects.

The goal is to reuse the modular FastAPI foundation and progressively introduce:

```text
FastAPI
   │
   ├── PostgreSQL
   ├── Authentication
   ├── Middleware
   ├── Async Processing
   ├── Streaming
   ├── LLM Integration
   └── Agentic AI
```

Each future project can add new routers, schemas, services, models, and integrations without putting everything into a single Python file.

---

## Development Principle

Keep responsibilities separated:

```text
Router       → HTTP/API handling
Schema       → Request/response validation
Service      → Business logic
Model        → Database structure
Database     → Database connection
Core         → Configuration
Main         → Application setup
```

This separation makes the project easier to understand, test, maintain, and extend.