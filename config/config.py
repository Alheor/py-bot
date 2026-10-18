from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    bot_token: str
    webhook_secret: str
    database_url: str

settings = Settings()