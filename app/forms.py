from dataclasses import dataclass


@dataclass
class GenerateForm:
    prompt: str
    content_type: str = "marketing"
    length: int = 300
    temperature: float = 0.7

    def validate(self):
        if not self.prompt or not self.prompt.strip():
            return False, "Prompt is required."
        if not (64 <= self.length <= 2000):
            return False, "Length must be between 64 and 2000."
        return True, None
