from fastapi import FastAPI, Response, Cookie
import redis 
import uuid

app = FastAPI()

@app.get("/")
def hello_world() -> dict:
    return {"message": "Hello World!!"}

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# /set/?key=mykey&value=myvalue
@app.get("/set/")
def set_value(key: str, value: str):
    r.set(key, value)
    return {"message": f"Key '{key}' set to value {value}"}

#/get/?key=mykey
@app.get("/get/")
def get_value(key: str):
    value = r.get(key)
    if value: 
        return {"key": key, "value": value}
    return {"message": f"Key '{key} not found"}

@app.get("/visits")
async def visits(response: Response, user_id: str = Cookie(default=None)) -> dict:
    if user_id is None:
        user_id = str(uuid.uuid4())
        print(user_id)
        response.set_cookie(key="user_id", value=user_id)
        visits = 0
    else:
        visits = r.get(f"visits:{user_id}")
        if visits is None:
            visits = 0
        else: 
            visits = int(visits)  
    visits += 1 
    r.set(f"visits:{user_id}", visits)
    return {"message": f"This endpoint has been visited {visits} times by user with ID {user_id}"}

    
