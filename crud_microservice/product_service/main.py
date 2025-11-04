from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()
engine = create_engine("sqlite:///./products.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
    total_price = Column(Float)
Base.metadata.create_all(engine)

@app.post("/add")
def add_product(name: str, price: float, quantity: int):
    db = Session()
    p = Product(name=name, price=price, quantity=quantity, total_price=price * quantity)
    db.add(p); db.commit(); db.close()
    return {"message": "Product added"}

@app.get("/get/{pid}")
def get_product(pid: int):
    db = Session()
    p = db.query(Product).filter(Product.id == pid).first()
    db.close()
    return p.__dict__

@app.post("/reduce/{pid}")
def reduce_stock(pid: int, qty: int):
    db = Session()
    p = db.query(Product).filter(Product.id == pid).first()
    p.quantity -= qty
    p.total_price = p.price * p.quantity
    db.commit(); db.close()
    return {"message": "Stock updated"}
