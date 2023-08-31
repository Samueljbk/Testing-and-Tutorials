from fastapi import FastAPI, HTTPException
from pathlib import Path
from pydantic import BaseModel
import numpy as np

app = FastAPI()


class User(BaseModel):
    name: str
    username: str
    email: str


@app.get("/hello")
def hello_world():
    return "Hello, World!"


@app.get("/items/{item_id}")
def obtain_item_id(item_id: int):
    return {"item_id": item_id}


@app.get("/users/{username}")
def view_profile(username: str):
    return {f"You're viewing {username}'s profile."}


@app.post("/users/create")
def create_user(user: User):
    return {"user": user}
