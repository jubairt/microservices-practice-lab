from fastapi import FastAPI
import requests

CONSUL_URL = "http://localhost:8500"

app = FastAPI()

def discover_service(service_name: str):
    """Fetch the service address from Consul dynamically."""
    url = f"{CONSUL_URL}/v1/catalog/service/{service_name}"
    res = requests.get(url).json()
    if res:
        service = res[0]
        address = service["ServiceAddress"]
        port = service["ServicePort"]
        return f"http://{address}:{port}"
    else:
        raise Exception(f"Service {service_name} not found")

@app.get("/orders")
def create_order():
    # Dynamically discover user & product services
    user_service = discover_service("user-service")
    product_service = discover_service("product-service")

    users = requests.get(f"{user_service}/users").json()
    products = requests.get(f"{product_service}/products").json()

    order = {
        "order_id": 1,
        "user": users[0],
        "product": products[0]
    }
    return order

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5002)
