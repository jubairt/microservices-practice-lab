from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/orders")
def create_order():
    users = requests.get("http://127.0.0.1:5000/users").json()
    products = requests.get("http://127.0.0.1:5001/products").json()

    order = {
        "order_id": 1,
        "user": users[0],
        "product": products[0]
    }
    return order
