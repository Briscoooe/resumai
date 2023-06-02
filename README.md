# ResumAI API

🔗 [https://resumai.fly.dev/docs](https://resumai.fly.dev/docs).

This is a [FastAPI](https://fastapi.tiangolo.com/) application that serves as the backend for the [ResumAI web app](https://www.brianbriscoe.dev/resume).

## Tech stack
The ResumAI API is built with [FastAPI](https://fastapi.tiangolo.com/) which itself uses [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation and [OpenAPI](https://swagger.io/specification/) for API documentation. The API is served by [Uvicorn](https://www.uvicorn.org/) and is deployed to [Fly.io](https://fly.io/).

The `/chat` endpoint magic is done via [LangChain](https://python.langchain.com/en/latest/index.html) which uses OpenAI's [GPT-3.5](https://openai.com/blog/openai-api/) to generate text. I feed my entire resume into the [prompt](https://github.com/Briscoooe/resumai/blob/main/chat.py#L36) on every request so that the bot can use it to generate responses.

## Notes
This is just for fun and a lot of steps have been skipped for the sake of convenience. If you want to copy or productise this, here are some optimisations I'd highly recommend:
- Fine-tune your own model using [OpenAI's fine-tuning](https://openai.com/blog/customizing-gpt-3) or something like [PrivateGPT](https://github.com/imartinez/privateGPT). Feeding the entire resume as JSON into the prompt every time like I do here is extremely token inefficient.
- Store conversations at least ephemerally so that the bot can remember context, this will also save tokens plus it's better UX. This is possible with LangChain but I haven't implemented it here.
- If you just want the chat interface and don't need the other endpoints, don't hardcode your entire resume as code into the repo. Use some something to extract all the text out of actual resumes in `.doc` or `.pdf` format and hope GPT-4 can map it to your schemas.

Additionally, as far as best practises goes there is no error handling and there are no tests.

## Todo
- [ ] Optimise prompt to remove unnecessary whitespace
- [ ] Use [LangChain conversations](https://python.langchain.com/en/latest/modules/memory/getting_started.html) to allow multiple messages within a single conversation
- [ ] Add response language support (maybe)
- [ ] Add bot persona support (maybe)