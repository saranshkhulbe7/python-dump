from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


p1 = Product(**{"id": 1, "name": "kjdsjlf", "price": 12.3})
