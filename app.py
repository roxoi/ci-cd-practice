from fastapi import FastAPI

app = FastAPI()

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to my Python API!"}

@app.get("/error") 
def error():
    return {"message": "Server error"}

# Define an endpoint that accepts a parameter
@app.get("/greet/{name}")
def greet_user(name: str):
    return {"greeting": f"Hello, {name}!"}

