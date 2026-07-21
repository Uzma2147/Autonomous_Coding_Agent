import google.generativeai as genai

from app.config import GEMINI_API_KEY
from app.ai.prompts import DIAGNOSIS_PROMPT


class LLMService:

    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def diagnose(self, title, description, code):

        prompt = DIAGNOSIS_PROMPT.format(
            title=title,
            description=description,
            code=code
        )

        response = self.model.generate_content(prompt)

        return response.text