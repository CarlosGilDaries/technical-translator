"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings sourced from the .env file.

    Attributes:
        groq_api_key: The Groq API key used to authenticate requests.
        groq_model: The Groq model to use for completions.
        groq_base_url: The Groq API base URL (OpenAI-compatible).
    """

    groq_api_key: str = ""
    groq_model: str = "llama-3.3-70b-versatile"
    groq_base_url: str = "https://api.groq.com/openai/v1"

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
