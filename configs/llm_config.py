import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

load_dotenv()
print("LANGSMITH:", os.getenv("LANGCHAIN_API_KEY"))
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    groq_api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.1
)