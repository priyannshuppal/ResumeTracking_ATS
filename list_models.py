import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # loads your GOOGLE_API_KEY from .env
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List available models
models = genai.list_models()

# Print models and their supported methods
for model in models:
    print(f"Model: {model.name}, Supported Methods: {model.supported_generation_methods}")
