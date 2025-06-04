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
    param_values = list() # Initialize an empty list to store parameter values

    for param_name in request.query_params.keys(): # Iterate over all query parameters
        param_values = request.query_params.getlist(param_name) # Get the values for each parameter
        for value in param_values:
            params.append({
                "name": param_name,
                "value": value
                })


    print(params) # Print the list of parameters to the console
    return {"params": params} 

from pydantic import BaseModel
from datetime import datetime
class Job(BaseModel):
    name: str
    cost: float
    

jobs = list()  # Initialize an empty list to store jobs
@app.post("/api/create") # Endpoint to create a job
def create(job: Job):
    jobs.append(job)

    return {"message": "Job created successfully", "job": job}

@app.get("/api/jobs") # Endpoint to read all jobs
def get_jobs():
    return {"jobs": jobs}

@app.delete("/api/delete/{job_no}") # Endpoint to delete a job by job no.
def delete(job_no: int):
    if 0 <= job_no < len(jobs):
        deleted_job = jobs.pop(job_no)
        return {"message": "Job deleted successfully", "job": deleted_job}
    else:
        return {"message": "Job not found"}, 404