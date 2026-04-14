"""Business logic for the translation feature.

Handles prompt building and Groq API calls (OpenAI-compatible SDK).
"""

from openai import OpenAI, APIConnectionError, APIStatusError, AuthenticationError

from core.config import settings

_PROMPTS: dict[str, str] = {
    "simple": "Explain the following technical text in simple, everyday terms:",
    "eli5": "Explain the following like I'm 10 years old:",
    "professional": "Rewrite the following in professional, non-technical language suitable for a business audience:",
    "analogies": "Use a creative analogy to explain the following technical concept:",
}

_DEFAULT_MODE = "simple"


def build_prompt(text: str, mode: str) -> str:
    """Build the user message for the OpenAI request.

    Args:
        text: The technical text provided by the user.
        mode: The explanation mode key.

    Returns:
        A formatted prompt string combining the mode instruction and the text.
    """
    instruction = _PROMPTS.get(mode, _PROMPTS[_DEFAULT_MODE])
    return f"{instruction}\n\n{text}"


def call_ai(prompt: str) -> str:
    """Send a prompt to Groq and return the response text.

    Args:
        prompt: The user message to send to the model.

    Returns:
        The model's response as a plain string.

    Raises:
        ValueError: If the GROQ_API_KEY is not configured.
        RuntimeError: If the Groq API returns an error or an unexpected response.
    """
    if not settings.groq_api_key:
        raise ValueError("GROQ_API_KEY is not set. Add it to your .env file.")

    client = OpenAI(
        api_key=settings.groq_api_key,
        base_url=settings.groq_base_url,
    )

    try:
        response = client.chat.completions.create(
            model=settings.groq_model,
            temperature=0.3,
            messages=[{"role": "user", "content": prompt}],
        )
    except AuthenticationError as exc:
        raise RuntimeError("Invalid Groq API key.") from exc
    except APIConnectionError as exc:
        raise RuntimeError("Could not connect to Groq API. Check your network.") from exc
    except APIStatusError as exc:
        raise RuntimeError(f"Groq API error {exc.status_code}: {exc.message}") from exc

    content = response.choices[0].message.content
    if content is None:
        raise RuntimeError("Groq returned an empty response.")

    return content.strip()
