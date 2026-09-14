from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_world")
def get_hello_world():
    return {"message": "Hello, World!"}
