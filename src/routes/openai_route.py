from fastapi import APIRouter
from openai_tech import fetch_it_news_openai
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/openai/news")
async def get_openai_news():
    try:
        response = fetch_it_news_openai()
        return JSONResponse(content={"news": response})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)