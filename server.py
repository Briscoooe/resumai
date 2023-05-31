from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from starlette.middleware.cors import CORSMiddleware

from chat import send_message
from db import my_resume
from schemas import (
    Resume,
    Experience,
    Education,
    OpenSourceContribution,
    RecentTechnologyCategory,
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/resume", response_model=Resume)
def get_my_resume():
    return my_resume


@app.get("/resume/experience", response_model=list[Experience])
def get_my_experience():
    return my_resume.experience


@app.get("/resume/education", response_model=list[Education])
def get_my_education():
    return my_resume.education


@app.get("/resume/open-source", response_model=list[OpenSourceContribution])
def get_my_open_source():
    return my_resume.open_source_contributions


@app.get("/resume/technologies", response_model=list[RecentTechnologyCategory])
def get_my_technologies():
    return my_resume.recent_technology_categories


@app.get("/chat")
def stream(query: str):
    return StreamingResponse(send_message(query), media_type="text/event-stream")
