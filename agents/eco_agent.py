# eco_trip_planner/agents/eco_agent.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.runnables import Runnable
from langchain.schema import StrOutputParser

# Load API key from .env
load_dotenv()

# Initialize Gemini via LangChain
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7
)

# Load prompt template from file
with open("prompts/eco_prompt.txt", "r") as file:
    prompt_text = file.read()

prompt = PromptTemplate.from_template(prompt_text)

# Build chain: Prompt → LLM → Output Parser
chain: Runnable = prompt | llm | StrOutputParser()

# Function used by Streamlit app
async def run_agent(data: dict) -> str:
    return chain.invoke(data)
