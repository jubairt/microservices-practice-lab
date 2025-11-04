from fastapi import FastAPI
import uvicorn
from register import register_service

app = FastAPI()

@app.get("/products")
def get_products():
    return [{"id": 101, "name": "Laptop"}, {"id": 102, "name": "Book"}]

@app.get("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    port = 5005
    register_service("product-service", port)
    uvicorn.run(app, host="0.0.0.0", port=port)
