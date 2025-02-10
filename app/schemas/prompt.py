from pydantic import BaseModel

class PromptRequest(BaseModel):
    idea: str  # User's rough prompt idea
    max_tokens: int = 100
    temperature: float = 0.7
    top_k: int = 40
    top_p: float = 0.9
