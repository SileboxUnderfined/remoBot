from pydantic_settings import BaseSettings
from pydantic import Field, BeforeValidator
from typing import Any, Annotated

def parse_comma_separated_list(value: Any) -> list[int]:
    if isinstance(value, str):
        return [int(item.strip()) for item in value.split(",")]
    return value

class Settings(BaseSettings):
    BOT_TOKEN: str = Field(...)
    ALLOWED_IDS: Annotated[list[int], BeforeValidator(parse_comma_separated_list)] = Field(...)

settings = Settings()