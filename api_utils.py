import os
from pydantic import BaseModel

class ChadInput(BaseModel):
    prompt : str
    api_key : str

def valid_api_key(external_key: str) -> bool:
    if external_key is not "":
        return (os.environ.get('API_KEY') == external_key)
    return False