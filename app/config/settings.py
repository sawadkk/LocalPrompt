import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Model Path
MODEL_PATH = os.getenv("MODEL_PATH", "../models/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

# ✅ Default Settings
DEFAULT_MAX_TOKENS = 100
DEFAULT_TEMPERATURE = 0.7
DEFAULT_TOP_K = 40
DEFAULT_TOP_P = 0.9
