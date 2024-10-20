from fastapi import FastAPI, Response, Cookie

app = FastAPI()

@app.get("/")
def hello_world() -> dict:
    return {"message": "Hello World!!"}

@app.get("/visits")
def visits(response: Response, visits: int = Cookie(default=0)) -> dict:
    visits += 1
    response.set_cookie(key="visits", value=str(visits))  
    return {"message": f"This endpoint has been visited {visits} number of times"}
    
