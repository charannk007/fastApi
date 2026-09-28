from fastapi import FastAPI

app = FastAPI(
    title="Learning API",
    description="An API for learning purposes",
    version="1.0.0",
)

@app.get("/")
async def test_endpoint():
    return {"message": "This is a test endpoint."}

@app.post("/echo")
async def echo_endpoint(data: dict):
    return {"echo": data}

@app.put("/update")
async def update_endpoint(data: dict):
    # Here you would typically update some resource with the provided data
    return {"updated_data": data}
