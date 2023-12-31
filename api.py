from gpt_versions import prompt_chad, prompt_normal, print_number
from fastapi import FastAPI, HTTPException, status, Request
import uvicorn 
import os 
from api_utils import ChadInput, valid_api_key, JobData
from dotenv import load_dotenv
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from redis import Redis
from rq import Queue
from rq.job import Job
from pydantic import BaseModel

load_dotenv()

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

redis_conn = Redis(host="localhost", port=6379)
task_queue = Queue("task_queue", connection = redis_conn)

@app.post('/chad_gpt')
@limiter.limit("12/minute")
def post(request : Request, input : ChadInput):
        input_key = input.api_key
        if not valid_api_key(external_key=input_key):
                raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect api key",
                headers={"WWW=Authenticate": "Basic"}
                )
        response = task_queue.enqueue(prompt_chad, input.prompt)
        
        while response.result == None:
                response = Job.fetch(response.id, connection = redis_conn)
        return {
             "succes": True,
             "job_id" : response.id,
             "result" : response.result,
        }

@app.post('/chad_gpt_noqueue')
@limiter.limit("12/minute")
def post(request : Request, input : ChadInput):
        input_key = input.api_key
        if not valid_api_key(external_key=input_key):
                raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect api key",
                headers={"WWW=Authenticate": "Basic"}
                )
        response = prompt_chad(input.prompt)
        
        return {
             "result" : response,
        }

@app.post('/highest_queue')
@limiter.limit("12/minute")
def post_job(request : Request, job: JobData):
        lowest = job.lowest
        highest = job.highest
        response = task_queue.enqueue(print_number, lowest, highest)
        
        while response.result == None:
                        response = Job.fetch(response.id, connection = redis_conn)
        return {
                "succes": True,
                "job_id" : response.id,
                "result" : response.result,
        }

@app.post('/highest_noqueue')
@limiter.limit("12/minute")
def post_job(request : Request, job: JobData):
        lowest = job.lowest
        highest = job.highest
        response = print_number(lowest, highest)
        return { "results" : response
        }

if __name__ == "__main__":
    uvicorn.run("api:app", host = os.environ.get('HOSTNAME'), reload = True)