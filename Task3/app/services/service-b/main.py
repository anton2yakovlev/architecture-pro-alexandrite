from fastapi import FastAPI

app = FastAPI()

@app.get("/get-shopping-cart-items")
def shopping_cart_items() -> list[dict]:
    return [
        {
            'id': 1,
            'name': 'Item 1',
            'price': 100,
            'quantity': 1
        },
        {
            'id': 2,
            'name': 'Item 2',
            'price': 200,
            'quantity': 2
        }
    ]