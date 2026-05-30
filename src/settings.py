from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, BeforeValidator
from typing import Any, Annotated
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

"""
def parse_comma_separated_list(value: Any) -> list[int] | Any:
    if isinstance(value, str):
        return [int(item.strip()) for item in value.split(",")]
    return value
"""

#CommaSeparetedList = Annotated[list[int], BeforeValidator(parse_comma_separated_list)]

class Settings(BaseSettings):
    BOT_TOKEN: str = Field(...)
    ALLOWED_IDS: int = Field(...)

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()