import os
from langchain_google_genai import ChatGoogleGenerativeAI
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

def get_gemini_news():
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=os.environ.get("GEMINI_API_KEY"))
        result = llm.invoke("What was a IT and Job market and Finace news story from today?")
        return result.content
    except Exception as e:
        return {"error": str(e)}