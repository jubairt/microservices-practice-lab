from fastapi import FastAPI
import uvicorn
import os
import sys
from register import register_service

app = FastAPI()

@app.get("/products")
def get_products():
    return [{"id": 101, "name": "Laptop"}, {"id": 102, "name": "Book"}]

@app.get("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    # Try to get port from command line or environment variable
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = int(os.getenv("PORT", 5005))

    register_service("product-service", port)
    uvicorn.run(app, host="0.0.0.0", port=port)
