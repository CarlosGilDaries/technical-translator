"""Translation API router.

Exposes POST /translate, delegating all logic to the translation service.
"""

from fastapi import APIRouter, HTTPException, status

from models.translation import TranslationRequest, TranslationResponse
from services.translation import build_prompt, call_ai

router = APIRouter()


@router.post("/translate", response_model=TranslationResponse, status_code=status.HTTP_200_OK)
def translate(request: TranslationRequest) -> TranslationResponse:
    """Translate technical text using the selected explanation mode.

    Args:
        request: The translation request containing text and mode.

    Returns:
        A TranslationResponse with the AI-generated plain-language result.

    Raises:
        HTTPException 400: If the mode is not recognised.
        HTTPException 503: If the OpenAI API is unavailable or misconfigured.
    """
    valid_modes = {"simple", "eli5", "professional", "analogies"}
    if request.mode not in valid_modes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid mode '{request.mode}'. Valid options: {sorted(valid_modes)}.",
        )

    prompt = build_prompt(request.text, request.mode)

    try:
        translated_text = call_ai(prompt)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail=str(exc)) from exc

    return TranslationResponse(translated_text=translated_text)
