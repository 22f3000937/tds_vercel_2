from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World!"}