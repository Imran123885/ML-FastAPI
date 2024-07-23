from pydantic import BaseModel

data = {
    'name': 'Murthy',
    'age': '28',
    'course': 'MLOps Bootcamp',
    'ratings': [3, 4, '4', '5', 4]
}

class Instructor(BaseModel):
    name: str
    age: int
    course: str
    ratings: list[int] = []

user = Instructor(**data)

print(f'Found an instructor: {user}')