from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import  ChatOpenAI
from langserve import add_routes
import openai
import os
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple api server using Langchain's Runnable interfaces",
)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(
    app,
    ChatOpenAI(model="gpt-3.5-turbo-1106"),
    path="/openai",
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
