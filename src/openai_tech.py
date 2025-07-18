import getpass
import os
from langchain_openai import ChatOpenAI
import pprint

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def fetch_it_news_openai():
    llm = ChatOpenAI(model="gpt-4.1-mini")
    tool = {"type": "web_search_preview"}
    llm_with_tools = llm.bind_tools([tool])
    response = llm_with_tools.invoke("What was a IT and Job market and Finace news story from today?")
    return response.content[0] if response.content else None