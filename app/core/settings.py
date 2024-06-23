from enum import Enum, unique
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


@unique
class Environments(str, Enum):
    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"


class ApiSettings(BaseModel):
    ADDRESS: str = "0.0.0.0"
    PORT: int = Field(8000, ge=0, le=65535)


class Config(BaseSettings):
    API: ApiSettings
    DEBUG: bool = False
    ENVIRONMENT: Environments = Environments.LOCAL

    class Config:
        env_nested_delimiter = "__"
        env_file = ".env.local"
        case_sensitive = True
        env_file_encoding = "utf-8"


config = Config()  # type: ignore[call-args]