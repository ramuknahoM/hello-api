from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/hello")
def get_hello():
    return {"message": "Hello, World!"}
