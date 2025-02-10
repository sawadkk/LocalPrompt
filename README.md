# 🚀 PromptMate - AI Prompt Engineer

PromptMate is an AI-powered tool designed to **refine and optimize** AI prompts, helping users generate high-quality, structured prompts that work effectively with advanced AI models.

## 📌 Features
- ✅ **Refines AI Prompts** - Converts rough ideas into **high-quality, structured prompts**  
- ✅ **Uses Mistral 7B** - Locally hosted **Mistral-7B-Instruct** for privacy and efficiency  
- ✅ **Customizable** - Supports different prompt **optimizations and fine-tuning**  
- ✅ **FastAPI Backend** - Simple API with easy-to-use **REST endpoints**  

## 📂 Folder Structure
```
PromptMate/
│️—— app/
│   ├—— api/                  # API Routes
│   │   ├—— prompt.py         # Prompt Engineering API
│   ├—— config/                 # Core Configurations
│   │   ├—— settings.py         # Environment & Settings
│   ├—— services/             # Business Logic
│   │   ├—— prompt_service.py # Prompt Processing Logic
│   └—— main.py               # FastAPI Entry Point
│️—— models/                    # AI Model Storage (Ignored in .gitignore)
│️—— .env                        # Environment Variables
│️—— .gitignore                  # Git Ignore File
│️—— requirements.txt            # Python Dependencies
│️—— README.md                   # Project Documentation
```

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/sawadkk/PromptMate.git
cd PromptMate
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Download Mistral 7B Model**
```bash
mkdir models
curl -L -o models/mistral-7b-instruct-v0.1.Q4_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-v0.1-GGUF/resolve/main/mistral-7b-v0.1.Q4_K_M.gguf?download=true
```

### **5️⃣ Run the API**
```bash
uvicorn app.main:app --reload
```

## 🔥 Usage
### **1️⃣ API Endpoint**
- **URL:** `POST /api/generate_prompt/`
- **Request:**
```json
{
    "idea": "Create a sci-fi world with AI robots.",
    "max_tokens": 100,
    "temperature": 0.7,
    "top_k": 40,
    "top_p": 0.9
}
```
- **Response:**
```json
{
    "original_idea": "Create a sci-fi world with AI robots.",
    "refined_prompt": "Design a detailed sci-fi world featuring advanced AI-driven civilizations...",
    "temperature": 0.7,
    "top_k": 40,
    "top_p": 0.9
}
```

## 📌 Future Enhancements
- 🔹 **Fine-tuning** - Train Mistral 7B for more **precise prompt refinement**  
- 🔹 **Web UI** - Add a **frontend interface** for prompt generation  
- 🔹 **Multi-model Support** - Integrate with **OpenAI, LLaMA, DeepSeek** for comparisons  

## ✨ Contributing
1. Fork the repository  
2. Create a new branch: `git checkout -b feature-name`  
3. Commit changes: `git commit -m "Added new feature"`  
4. Push to branch: `git push origin feature-name`  
5. Open a **Pull Request** 🎉  



