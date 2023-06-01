from fastapi import FastAPI, Query
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


@app.get("/resume", response_model=Resume, summary="Get my resume")
def get_my_resume():
    return my_resume


@app.get(
    "/resume/experience", response_model=list[Experience], summary="Get my experience"
)
def get_my_experience():
    return my_resume.experience


@app.get(
    "/resume/education", response_model=list[Education], summary="Get my education"
)
def get_my_education():
    return my_resume.education


@app.get(
    "/resume/open-source",
    response_model=list[OpenSourceContribution],
    summary="Get my open source contributions",
)
def get_my_open_source():
    return my_resume.open_source_contributions


@app.get(
    "/resume/technologies",
    response_model=list[RecentTechnologyCategory],
    summary="Get my recent technologies",
)
def get_my_technologies():
    return my_resume.recent_technology_categories


@app.get("/chat", summary="Chat about my resume with a magic AI bot")
def chat(
    message: str = Query(
        default="Summarise Brian",
        description="Your message to the bot",
        example="What university did Brian go to?",
    ),
    persona: str = Query(
        default="normal",
        description="The persona of the bot",
        example="normal",
        regex="^(normal|friendly|poet|rapper)$",
    ),
    language: str = Query(
        default="en",
        description="The language of the bot",
        example="en",
        regex="^(en|fr|es|de|it|pt)$",
    ),
):
    return StreamingResponse(
        send_message(message=message, persona=persona, language=language),
        media_type="text/event-stream",
    )
