import os
from pydantic import BaseModel
from dotenv import load_dotenv
 
load_dotenv()

class ChadInput(BaseModel):
    prompt : str
    api_key : str

def valid_api_key(external_key: str) -> bool:
    if external_key != "":
        return (os.environ.get('API_KEY') == external_key)
    return False

class JobData(BaseModel):
        lowest : int
        highest: int