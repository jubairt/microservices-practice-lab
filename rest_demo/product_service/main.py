from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

# ✅ Create FastAPI app normally
app = FastAPI()

# ✅ Create and configure instrumentator
instrumentator = Instrumentator()

# ✅ Define routes
@app.get("/products")
def get_products():
    return [
        {"id": 101, "name": "Laptop"},
        {"id": 102, "name": "Book"},
    ]

# ✅ Instrument and expose metrics
instrumentator.instrument(app).expose(app)
