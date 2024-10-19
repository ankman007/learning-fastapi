from fastapi import FastAPI
import json

with open('data.json', 'r') as file:
    fake_db = json.load(file)

app = FastAPI()

@app.get("/")
def hello_world() -> dict:
    return {"message": "Hello World"}

@app.get("/login")
def login(username: str, password: str) -> dict:
    for user_id, user_data in fake_db["users"].items():
        if user_data["username"] == username and user_data["password"] == password:
            return {
                "message": "User logged in successfully",
                "user_info": {"name": user_data["name"], "age": user_data["age"], "id": user_id}
            }

    return {"message": "Login Failed"}
