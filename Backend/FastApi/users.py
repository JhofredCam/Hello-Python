from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Entidad user

class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

users_list = [
    User(id=1,name="Carlos", surname="Hernández", url="https://example.com/carlos-hernandez", age=30),
    User(id=2,name="María", surname="Gómez", url="https://example.com/maria-gomez", age=25),
    User(id=3,name="Luis", surname="Pérez", url="https://example.com/luis-perez", age=35)
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

@app.get("/user/{id}")
async def user(id: int):
    search_user(id)
    

@app.get("/user/")
async def user(id: int):
    try:
        user = filter(lambda user :  user.id == id, users_list)
        return list(user)[0]
    except:
        return {"Error":"Not valid id"}

@app.post("/user/", response_model=User, status_code=201)
async def user(user: User): # automaticamente convierte json a objeto tipo User
    #agregarlo a la base de datos
    if type(search_user(user.id)) == User:
        raise HTTPException(404, detail="User already exists")
        # return {"Error":"User already exists"}
    add_user(user)
    return user

@app.put("/user/")
async def user(user: User):

    for index in range(0,len(users_list)):
        if users_list[index].id == user.id:
            users_list[index] = user
            return {"User edited" : user}
    
    return {"Error" : "User not found"}

@app.delete("/user/{id}")
async def user(id: int):
    dropped_user = delete_user(id)
    if dropped_user is False:
        return {"Error":"User not found"}
    return dropped_user


def delete_user(id):
    for index, user in enumerate(users_list):
        if id == user.id:
            return users_list.pop(index)
    return False


def search_user(id):
    try:
        user = filter(lambda user :  user.id == id, users_list)
        return list(user)[0]
    except:
        return {"Error":"Not valid id"}

def add_user(user):
    users_list.append(user)