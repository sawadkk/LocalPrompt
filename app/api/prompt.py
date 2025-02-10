from fastapi import APIRouter
from app.schemas.prompt import PromptRequest
from app.services.prompt_service import generate_refined_prompt

# ✅ Initialize API Router
router = APIRouter(prefix="/api", tags=["Prompt Engineer"])

@router.post("/generate_prompt/")
def generate_prompt(request: PromptRequest):
    """API endpoint to generate a better AI prompt."""
    refined_prompt = generate_refined_prompt(
        request.idea,
        request.max_tokens,
        request.temperature,
        request.top_k,
        request.top_p
    )
    return {
        "original_idea": request.idea,
        "refined_prompt": refined_prompt,
        "temperature": request.temperature,
        "top_k": request.top_k,
        "top_p": request.top_p
    }
