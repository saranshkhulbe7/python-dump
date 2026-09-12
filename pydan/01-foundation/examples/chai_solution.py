from pydantic import BaseModel
from typing import 

class Lesson(BaseModel):
    lesson_id: int
    topic: str


class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]
