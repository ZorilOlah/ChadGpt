import openai
import argparse
from gpt_versions import prompt_chad, prompt_normal
from fastapi import FastAPI, HTTPException, status
import uvicorn 
import os 
from api_utils import ChadInput, valid_api_key
from dotenv import load_dotenv

# parser = argparse.ArgumentParser()
# parser.add_argument("ChadGPT Prompt", type=str, nargs='+', help = "Your text prompt to ChadGPT. Ask a question.")
# prompt = parser.parse_args()

load_dotenv()

app = FastAPI()

@app.post('/chad_gpt')
async def post(input : ChadInput):
        input_key = input.api_key
        if not valid_api_key(external_key=input_key):
                raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect api key",
                headers={"WWW=Authenticate": "Basic"}
                )
        response = prompt_chad(input)
        return {response}

if __name__ == "__main__":
    uvicorn.run("api:app", host = os.environ.get('HOSTNAME'), reload = True)