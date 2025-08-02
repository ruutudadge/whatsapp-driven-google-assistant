import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Summarize this document in bullet points."},
            {"role": "user", "content": text}
        ],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']
