from enum import StrEnum
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

class SSHAuthType(StrEnum):
    SSH_AGENT = "ssh_agent"
    SSH_AGENT_ENVIRONMENT = "ssh_agent_environment"
    SSH_KEYS = "ssh_keys"

class Settings(BaseSettings):
    BOT_TOKEN: str = Field(...)
    ALLOWED_IDS: CommaSeparatedList[int] = Field(...)
    PROXY_URL: str | None = None
    SSH_AUTH_METHODS: CommaSeparatedList[SSHAuthType] = [SSHAuthType.SSH_AGENT,SSHAuthType.SSH_AGENT_ENVIRONMENT]
    SSH_AGENT_PATH: str | None = None
    SSH_KEYS_PATH: CommaSeparatedList[str] | None = None

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8"
    )

settings = Settings()