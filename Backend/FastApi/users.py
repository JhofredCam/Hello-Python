from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Entidad user

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(name="Carlos", surname="Hernández", url="https://example.com/carlos-hernandez", age=30),
    User(name="María", surname="Gómez", url="https://example.com/maria-gomez", age=25),
    User(name="Luis", surname="Pérez", url="https://example.com/luis-perez", age=35)
]

@app.get("/usersjson")
async def usersjson():
    return [
    {"name": "Carlos", "surname": "Hernández", "url": "https://example.com/carlos-hernandez", "age":25},
    {"name": "María", "surname": "Gómez", "url": "https://example.com/maria-gomez", "age":35},
    {"name": "Luis", "surname": "Pérez", "url": "https://example.com/luis-perez", "age":19},
]

@app.get("/users")
async def users():
    return users_list