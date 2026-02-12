from pydantic import BaseModel

class product(BaseModel):
    name: str
    price: float
    in_stock: bool

data = {
    "name": "laptop",
    "price": 499.99,
    "in_stock": True
}

product = product(**data)
print(product)


bad_data = {
    "name": "laptop",
    "price": "three",
    "in_stock": True
}

bad_product = product(**bad_data)
print(bad_product)