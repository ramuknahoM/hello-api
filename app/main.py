from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_hi", response_model=dict)
async def hello_hi():
    return {"message": "Hello, hi!"}

# Existing routes can be added below this line
