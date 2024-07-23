from fastapi import FastAPI  

app = FastAPI()

@app.get('/') # path operation decorator
async def root():
    return {'message': 'Hello world from fastapi'}

@app.get('/sigma') # path operation decorator
def root():
    return {'message': 'You have reached the sigma'}