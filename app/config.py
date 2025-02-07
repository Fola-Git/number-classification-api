from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_VERSION: str = "v1"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()