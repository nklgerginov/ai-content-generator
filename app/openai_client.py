import os
import openai
from typing import Dict, Any

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    openai.api_key = None
else:
    openai.api_key = OPENAI_API_KEY


class OpenAIClient:
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model

    def generate(
        self, prompt: str, max_tokens: int = 512, temperature: float = 0.7
    ) -> Dict[str, Any]:
        if not openai.api_key:
            return {"error": "OPENAI_API_KEY not configured"}

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful copywriter."},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=max_tokens,
                temperature=temperature,
            )
            text = response["choices"][0]["message"]["content"]
            return {"text": text, "meta": {"usage": response.get("usage")}}

        except openai.error.OpenAIError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": "Unexpected error: " + str(e)}
