from fastapi import FastAPI

app = FastAPI()

@app.get("/hello_world_i_am_mk", response_model=dict)
def hello_world_i_am_mk():
    return {"message": "Hello, world! I am mk"}

# Existing routes can be added below
