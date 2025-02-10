from llama_cpp import Llama
from app.config.settings import MODEL_PATH

# ✅ Load Mistral 7B Model
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,          # Maximum tokens per generation
    n_gpu_layers=30,     # Optimized for GTX 1650 (4GB VRAM)
    verbose=False
)

def generate_refined_prompt(user_idea: str, max_tokens: int, temperature: float, top_k: int, top_p: float) -> str:
    """Refines a rough prompt idea into a structured, high-quality AI prompt."""

    system_instruction = (
        "You are an expert AI prompt engineer. Your task is to take the given prompt idea "
        "and refine it into a structured, high-quality AI prompt that will work effectively with "
        "advanced AI models. Ensure clarity, specificity, and optimal creativity in the response.\n\n"
        "### Example Format:\n"
        "- **Original Idea**: Generate a futuristic city image.\n"
        "- **Refined Prompt**: Create a high-resolution image of a futuristic city with neon skyscrapers, "
        "flying cars, and cyberpunk-style street markets. Use a vibrant color palette with glowing neon lights.\n\n"
        "### User Idea:\n"
        f"- **Original Idea**: {user_idea}\n"
        "- **Refined Prompt**:"
    )

    # ✅ Generate response from Mistral 7B
    response = llm(
        system_instruction,
        max_tokens=max_tokens,
        temperature=temperature,
        top_k=top_k,
        top_p=top_p
    )

    # ✅ Extract refined prompt from AI response
    return response["choices"][0]["text"].strip()
