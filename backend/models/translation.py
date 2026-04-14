"""Pydantic schemas for the translation feature."""

from pydantic import BaseModel, Field


class TranslationRequest(BaseModel):
    """Request body for the /translate endpoint.

    Attributes:
        text: The technical text to be translated.
        mode: The explanation mode. One of 'simple', 'eli5', 'professional', 'analogies'.
    """

    text: str = Field(..., min_length=1, description="Technical text to translate.")
    mode: str = Field(
        default="simple",
        description="Explanation mode: simple | eli5 | professional | analogies.",
    )


class TranslationResponse(BaseModel):
    """Response body returned by the /translate endpoint.

    Attributes:
        translated_text: The AI-generated plain-language version of the input.
    """

    translated_text: str
