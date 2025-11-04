from fastapi import FastAPI
import requests

app = FastAPI()
PRODUCT_URL = "http://localhost:8000"

@app.post("/order")
def place_order(pid: int, qty: int):
    product = requests.get(f"{PRODUCT_URL}/get/{pid}").json()
    requests.post(f"{PRODUCT_URL}/reduce/{pid}?qty={qty}")
    total = product["price"] * qty
    return {
        "message": "Order placed",
        "product": product["name"],
        "qty": qty,
        "unit_price": product["price"],
        "total": total
    }
