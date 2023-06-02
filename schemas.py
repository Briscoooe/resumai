import json
from datetime import date

from pydantic import BaseModel


class Experience(BaseModel):
    company: str
    title: str
    start_date: date
    end_date: date
    skills: list[str]
    summary: str
    location: str


class Education(BaseModel):
    school: str
    degree: str
    start_date: date
    end_date: date


class RecentTechnologyCategory(BaseModel):
    title: str
    technologies: list[str]


class PersonalProject(BaseModel):
    title: str
    description: str
    technologies: list[str]
    link: str


class OpenSourceContribution(BaseModel):
    title: str
    description: str
    link: str


class Resume(BaseModel):
    name: str
    github: str
    linkedin: str
    experience: list[Experience]
    education: list[Education]
    recent_technology_categories: list[RecentTechnologyCategory]
    personal_projects: list[PersonalProject]
    open_source_contributions: list[OpenSourceContribution]

    @property
    def experience_json(self) -> str:
        return json.dumps([e.json() for e in self.experience])

    @property
    def education_json(self) -> str:
        return json.dumps([e.json() for e in self.education])

    @property
    def recent_technology_categories_json(self) -> str:
        return json.dumps([c.json() for c in self.recent_technology_categories])

    @property
    def personal_projects_json(self) -> str:
        return json.dumps([p.json() for p in self.personal_projects])

    @property
    def open_source_contributions_json(self) -> str:
        return json.dumps([c.json() for c in self.open_source_contributions])
