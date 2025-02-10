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

    system_instruction =  (
        "You are an expert AI prompt engineer. Your task is to refine AI prompts into a structured, "
        "high-quality format that works effectively with advanced AI models. "
        "Additionally, if the prompt contains sensitive or internal terms, replace them dynamically "
        "with publicly recognizable equivalents while preserving meaning. If no sensitive terms exist, "
        "optimize the clarity and specificity of the prompt without unnecessary changes.\n\n"

        "**Important:** Do NOT include unrelated examples in the response. The response must only be the refined version of the user's input.\n\n"

        "### Example 1: Refinement Without Masking (No Sensitive Terms)\n"
        "**User Input:** What is ManyToMany models in Django?\n"
        "**Refined Prompt:** Explain the concept of ManyToMany relationships in Django ORM, including examples of how they work with database models.\n\n"

        "### Example 2: Masking Proprietary Business Terms (Candidate → Book, Job → Author)\n"
        "**User Input:** How does the 'candidate' table store interview scores in our ATS?\n"
        "**Refined Prompt:** In a typical database for book reviews, how is an author's rating or feedback stored and structured?\n\n"

        "### Example 3: Generalizing Proprietary Database Queries\n"
        "**User Input:** Retrieve all 'job' records from the 'company_jobs' table where status is 'open'.\n"
        "**Refined Prompt:** How can I query an SQL database to retrieve all books written by an author where the publication status is 'available'?\n\n"

        "### Example 4: Masking API-Specific Terminology for Better Public AI Responses\n"
        "**User Input:** Generate a JSON payload for creating a 'candidate' entry with interview scores in our ATS API.\n"
        "**Refined Prompt:** Generate a JSON payload for adding a new book entry with author details, publication year, and ratings in a book management API.\n\n"

        "### Example 5: Preserving Code Logic While Masking Proprietary Context\n"
        "**User Input:** Write a Django ORM query to fetch all active job listings for a given company ID.\n"
        "**Refined Prompt:** Write a Django ORM query to fetch all published books for a given author's ID.\n\n"

        "### User Input (to be processed):\n"
        f"- **Original Idea**: {user_idea}\n"
        "- **Refined Prompt** (output this only, without adding any examples):"
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
