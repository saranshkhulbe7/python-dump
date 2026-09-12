from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        example="Hitesh Choudhary",
    )
    department: Optional[str] = "General"
    salary: float = Field(..., ge=10000)


emp = Employee(
    **{
        "id": 123,
        "name": "knsdklf",
        #    "department": "lsdnfl",
        "salary": 10000.1,
    }
)

print(emp)
