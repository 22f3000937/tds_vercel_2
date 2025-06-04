from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/api/params")
def search(request: Request):
    params = list() # Initialize an empty list to store parameters

    for param_name in request.query_params.keys(): # Iterate over all query parameters
        params.append(param_name) # Append each parameter name to the list

    print(params) # Print the list of parameters to the console
    return {"params": params} 