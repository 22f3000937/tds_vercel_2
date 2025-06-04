from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World!"}