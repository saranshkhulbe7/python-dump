from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {"id": 1, "name": "ChaiCode", "is_active": True}

print(**input_data)
# print(user)
