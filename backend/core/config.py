"""Application configuration loaded from environment variables."""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """App settings sourced from the .env file.

    Attributes:
        openai_api_key: The OpenAI API key used to authenticate requests.
    """

    openai_api_key: str = ""

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
