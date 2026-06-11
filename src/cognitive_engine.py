import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_safety_summary(drug, fda_data):

    prompt = f"""
Drug: {drug}

FDA Signals:
{fda_data}

Provide:

1. Safety Summary
2. Common Risks
3. Recommendation

Keep it concise.
"""

    response = model.generate_content(prompt)

    return response.text