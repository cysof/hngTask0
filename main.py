from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pytz

app = FastAPI()

class APIResponse(BaseModel):
    email: str
    current_datetime: str
    github_url: str
    
@app.get("/home", response_model=APIResponse)
async def get_info():
    """
    Retrieve and return information including email, current datetime, and GitHub URL.

    This function handles GET requests to the '/home' endpoint. It returns a JSON
    object containing the registered email address, the current datetime in UTC
    (formatted according to ISO 8601), and the GitHub URL of the project.
    Returns:
        APIResponse: A Pydantic model containing:
            - email (str): The registered email address.
            - current_datetime (str): The current UTC datetime in ISO 8601 format.
            - github_url (str): The URL of the project's GitHub repository.
    """
    return {
        "email": "cysofthome@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).strftime('%Y-%m-%dT%H:%M:%SZ'),
        "github_url": "https://github.com/cysof/hngTask0",
    }
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)