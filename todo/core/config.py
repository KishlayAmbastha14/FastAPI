from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
  DATABASE_URL : str
  model_config = SettingsConfigDict(env_file = ".env")
    # extra = "ignore"
  


settings = Settings()


## FUTURE SCOPE TO ADD

# class Settings(BaseSettings):
#     # App
#     APP_NAME: str = "AI Backend"
#     ENV: str = "development"
#     DEBUG: bool = True

#     # Database
#     DATABASE_URL: str

#     # Security
#     SECRET_KEY: str
#     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

#     # AI / LLM
#     GEMINI_API_KEY: str | None = None
#     OPENAI_API_KEY: str | None = None

#     # Redis / Cache
#     REDIS_URL: str | None = None

#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )