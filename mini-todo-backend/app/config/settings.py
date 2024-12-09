from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# Load the .env file
load_dotenv()


class DatabaseSettings(BaseSettings):
    DB_TYPE: str
    DB_USERNAME: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DATABASE_URL: str = ""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")


class AuthSettings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")


# Create an instance of the settings to use in your app
db_settings = DatabaseSettings()
db_settings.DATABASE_URL = f"{db_settings.DB_TYPE}://{db_settings.DB_USERNAME}:{db_settings.DB_PASSWORD}@{db_settings.DB_HOST}:{db_settings.DB_PORT}/{db_settings.DB_NAME}"

auth_settings = AuthSettings()
