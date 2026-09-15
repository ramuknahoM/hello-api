from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/hello_hi')
def hello_hi():
    return {'message': 'Hello, Hi!'}
