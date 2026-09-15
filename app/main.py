from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_hi")
def hello_hi():
    return {"message": "Hello, Hi!"}
