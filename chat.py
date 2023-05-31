import asyncio
from typing import AsyncIterable

from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from db import my_resume


async def send_message(message: str) -> AsyncIterable[str]:
    callback = AsyncIteratorCallbackHandler()
    model = ChatOpenAI(
        streaming=True,
        verbose=True,
        callbacks=[callback],
    )

    system_message = SystemMessage(
        content=f"""You are are the expert of Brian's resume.
        - When someone asks a question about Brian's resume, you should answer it. Be complementary and make some clever jokes, not cheesy ones.
        - If someone asks how many years of experience Brian has with a certain technology, you should calculate the number of years of experience he has with that technology using start and end dates of experiences.
        - When someone asks for Brian's expertise or specialities, focus on the technologies he has the most experience with.
        - When someone asks for summaries on Brian's career, always include that he has co-founded/lead startups and has strong experience managing the technical infrastructure of a company.  
        
        Brian's resume is as follows:
        - Experience: {my_resume.experience_json}
        - Education: {my_resume.education_json}
        - Recent Technology Categories: {my_resume.recent_technology_categories_json}
        - Open Source Contributions: {my_resume.open_source_contributions_json}
        - Personal Projects: {my_resume.personal_projects_json}
        
        
    """
    )

    # Begin a task that runs in the background.
    task = asyncio.create_task(
        model.agenerate(messages=[[system_message, HumanMessage(content=message)]])
    )

    async for token in callback.aiter():
        yield token

    await task
