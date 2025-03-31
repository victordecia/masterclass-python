from fastapi import APIRouter
from controllers.translate_controller import translate_text, TextRequest

router = APIRouter()

@router.post("/translate")
async def translate(request: TextRequest):
    return translate_text(request)
