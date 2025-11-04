from fastapi import FastAPI
import uvicorn
from register import register_service

app = FastAPI()

@app.get("/users")
def get_users():
    return [{"id": 1, "name": "Jubi"}, {"id": 2, "name": "Alex"}]

@app.get("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    port = 5000  # try changing this later to test auto-update
    register_service("user-service", port)
    uvicorn.run(app, host="0.0.0.0", port=port)
