from fastapi import APIRouter, Response, status
from src.config.db import conn
from src.models.user import users
from src.schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get("/users", response_model=list[User], tags=["users"])
def get_users(): 
    return conn.execute(users.select()).mappings().fetchall()

@user.post("/user", response_model=User, tags=["users"])
def create_user(user: User):
    new_user = {"id": user.id,"name": user.name, "email": user.email}
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    obj = conn.execute(users.select().where(users.c.id == result.lastrowid)).mappings().first()
    return obj 

@user.get("/user/{id}", response_model=User, tags=["users"])
def get_user(id: str): 
    return conn.execute(users.select().where(users.c.id == id)).mappings().first()

@user.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
def delete_user(id: str): 
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/user/{id}", response_model=User, tags=["users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name= user.name, email= user.email).where(users.c.id == id))
    conn.commit()
    return conn.execute(users.select().where(users.c.id == id)).mappings().first()