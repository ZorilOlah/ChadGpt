import openai
import argparse
from gpt_versions import prompt_chad, prompt_normal
from fastapi import FastAPI
import uvicorn 
import os 

# parser = argparse.ArgumentParser()
# parser.add_argument("ChadGPT Prompt", type=str, nargs='+', help = "Your text prompt to ChadGPT. Ask a question.")
# prompt = parser.parse_args()

app = FastAPI()

@app.post('/chad_gpt')
async def post(text):
        response = prompt_chad(text)
        return {response}

if __name__ == "__main__":
    uvicorn.run("api:app", host = os.environ.get('HOSTNAME'), reload = True)