from pydantic_settings import BaseSettings, SettingsConfigDict, NoDecode
from pydantic import Field, BeforeValidator
from typing import Any, Annotated, Callable, TypeVar
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

T = TypeVar('T')

CommaSeparatedList = Annotated[
    list[T], 
    NoDecode, 
    BeforeValidator(
        lambda v: 
            [item.strip() for item in v.split(",") if item.strip()] 
            if isinstance(v, str) 
            else v
    )
]

class Settings(BaseSettings):
    BOT_TOKEN: str = Field(...)
    ALLOWED_IDS: CommaSeparatedList[int] = Field(...)
    PROXY_URL: str | None = None

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()