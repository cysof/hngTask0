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
    
@app.get("/", response_model=APIResponse)
async def get_info():
    return {
        "email": "cysofthome@gmail.com",
        "current_datetime": datetime.now(pytz.UTC).isoformat(),
        "github_url": "https://github.com/cysof/hngTask0",
        
    }

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)