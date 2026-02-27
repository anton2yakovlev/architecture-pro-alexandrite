import requests

from fastapi import FastAPI

app = FastAPI()

@app.get("/get-total-price")
def read_root() -> float:
    response = requests.get("http://service-b:7002/get-shopping-cart-items")
    shopping_cart_items = response.json()
    total_price = sum(item['price'] * item['quantity'] for item in shopping_cart_items)
    return float(total_price)