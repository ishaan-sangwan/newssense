import getpass
import os 
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your google api key: ")

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    temperature=1,
    max_tokens=None,
    timeout=None,
    max_retries=2
)


