from transformers import pipeline

llm = pipeline("text-generation", model="google/flan-t5-large")

def generate_response(query, risk, recommendation, context):
    prompt = f"""
    You are a healthcare assistant.

    Patient has: {query}
    Risk level: {risk}

    Use this medical knowledge:
    {context}

    Give short, clear medical advice.
    Do NOT mention context or instructions.
    """

    output = llm(prompt, max_new_tokens=80)[0]['generated_text']
    return output.strip()
