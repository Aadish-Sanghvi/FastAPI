from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
    return {'message': 'Hello, World!'}

@app.get('/about')
def hello():
    return {'message': 'about section!'}

# uvicorn 1_INTRO.main:app --reload
# http://127.0.0.1:8000/docs