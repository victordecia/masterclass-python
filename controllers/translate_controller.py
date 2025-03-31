from services.translation_service import consonant_translation
from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

def translate_text(request: TextRequest):
    translated_text = consonant_translation(request.text)
    return {"translated_text": translated_text}
