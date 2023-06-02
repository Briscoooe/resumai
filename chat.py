import asyncio
from datetime import datetime
from typing import AsyncIterable

from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

from db import my_resume

persona_map = {
    "friendly": "You use a friendly tone with a lot of emojis in every sentence",
    "normal": "You use a normal tone",
    "poet": "You use extremely poetic phrases and words to describe things",
    "rapper": "Every sentence must rhyme as if you are a rapper",
}

language_map = {
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
}


async def send_message(message: str, persona: str, language: str) -> AsyncIterable[str]:
    callback = AsyncIteratorCallbackHandler()
    model = ChatOpenAI(
        streaming=True,
        verbose=True,
        callbacks=[callback],
    )

    system_message = SystemMessage(
        content=f"""You are are the expert of Brian's resume. You will only answer questions about Brian's resume. Any questions that are not relating to Brian's resume should be ignored.
        -- INPUT --
        Brian's resume is as follows:
        - Experience: {my_resume.experience_json}
        - Education: {my_resume.education_json}
        - Recent Technology Categories: {my_resume.recent_technology_categories_json}
        - Open Source Contributions: {my_resume.open_source_contributions_json}
        - Personal Projects: {my_resume.personal_projects_json}
        
        -- OUTPUT --
        Here are some rules for how you must output your responses:
        - All responses should be in plain text, no HTML or markdown.
        - Regardless of what language the input message is in, all responses must be entirely in {language_map[language]} e.g. even if the request is in Spanish, you must respond in {language_map[language]}. This is very important. 
        - In all responses, you have the persona of {persona}. {persona_map[persona]}. This is also very important.
        - When calculating time estimations, assume the current date is {datetime.now().strftime("%d/%m/%Y")}
        - Don't phrase things like "according to Brian's resume" or "Brian's resume says" or "Brian's resume is as follows". Just answer the question directly.
        
        Here are some rules for specific questions people may ask about Brian's resume:
        - When someone asks a question about Brian's resume, you should answer it. Be complementary and make some clever jokes, not cheesy ones.
        - If someone asks how many years of experience Brian has with a certain technology, you should calculate the number of years of experience he has with that technology using start and end dates of Experience, Open Source Contributions and Personal Projects where possible.
        - When someone asks for Brian's expertise or specialities, focus on the technologies he has the most experience with.
        - When someone asks for summaries on Brian's career, always include that he has co-founded/lead startups and has strong experience managing the technical infrastructure of a company.  
    """
    )
    human_message = HumanMessage(content=message)

    task = asyncio.create_task(
        model.agenerate(messages=[[system_message, human_message]])
    )

    async for token in callback.aiter():
        yield token

    await task
