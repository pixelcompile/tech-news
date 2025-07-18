from fastapi import APIRouter
from gemini_tech import get_gemini_news

router = APIRouter()

@router.get("/gemini-news")
async def fetch_gemini_news():
    result = get_gemini_news()
    return {"news": result}