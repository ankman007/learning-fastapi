from fastapi import FastAPI

fake_db = {
    "users": {
        "user1": {
            "username": "admin",
            "password": "admin", 
            "name": "Ankit",
            "age": 11,
        },
        "user2": {
            "username": "btn",
            "password": "btn",
            "name": "Jamun",
            "age": 250,
        },
    }
}

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.get("/login")  
def login(username: str, password: str):
    user = fake_db["users"].get(username)
    if user and user["password"] == password:  
        return {
            "message": "User logged in successfully",
            "user_info": {"name": user["name"], "age": user["age"]}
        }
    else:
        return {"message": "Login Failed"}
