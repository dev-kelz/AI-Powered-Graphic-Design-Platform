from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = BACKEND_ROOT.parent
FRONTEND_TEMPLATES = PROJECT_ROOT / "frontend" / "templates"
FRONTEND_STATIC = PROJECT_ROOT / "frontend" / "static"


class Settings(BaseSettings):
    app_name: str = "Kelz Graphics Studio"
    secret_key: str = "crgrgqgj9'''''affhanrqepggehisndrhfuqergqelgjrg''''lfawfnoafqroduction"
    database_url: str = "sqlite:///./kelz_graphics.db"
    upload_dir: str = "uploads"

    model_config = SettingsConfigDict(env_file=BACKEND_ROOT / ".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
