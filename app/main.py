from fastapi import FastAPI
from app.api import prompt

# ✅ Initialize FastAPI App
app = FastAPI(title="PromptMate - AI Prompt Engineer", version="1.0")

# ✅ Include API routes
app.include_router(prompt.router)

# ✅ Run API: `uvicorn app.main:app --reload`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
