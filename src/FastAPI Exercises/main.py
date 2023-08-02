from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    username: str
    email: str


@app.get("/hello")
def hello_world():
    return "Hello, World!"


@app.get("/items/{item_id}")
def obtain_item_id():
    return "{item_id}"


@app.get("/users/")
def view_profile(username: str):
    return {"You're viewing {username}'s profile."}


@app.post("/users/create")
def create_user(user: User):
    return {"user": user}
