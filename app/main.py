from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_vanakam", response_model=dict)
async def hello_vanakam():
    return {"message": "Vanakam!"}
