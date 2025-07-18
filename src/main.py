from fastapi import FastAPI
from routes.openai_route import router as openai_router
from routes.gemini_route import router as gemini_router

app = FastAPI()

app.include_router(openai_router, prefix="/openai", tags=["OpenAI"])
app.include_router(gemini_router, prefix="/gemini", tags=["Gemini"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tech News API!"}