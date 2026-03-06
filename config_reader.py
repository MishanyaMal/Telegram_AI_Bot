from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
	BOT_TOKEN: SecretStr
	BASE_URL_FROM_OPENROUTER: SecretStr
	API_KEY_OF_CLIENT: SecretStr
	API_OF_MODEL: SecretStr
	model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

config = Settings()