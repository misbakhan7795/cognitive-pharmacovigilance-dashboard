import google.generativeai as genai

genai.configure(
    api_key="YOUR_API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

def generate_safety_summary(
    drug,
    sentiment,
    faers_results
):

    prompt = f"""
Drug:
{drug}

Patient Sentiment:
{sentiment}

FDA Evidence:
{faers_results}

Generate:

1. Safety Summary

2. Major Risks

3. Confidence Level

4. Recommendation
"""

    response = model.generate_content(
        prompt
    )

    return response.text