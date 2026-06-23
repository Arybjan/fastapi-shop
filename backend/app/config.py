from pydantic_settings import BaseSettings
from typing import Union, List


class Settings(BaseSettings):
    app_name: str = "Shop FastAPI"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: Union[List[str], str] = [
        "localhost:5173",
        "localhost:3000",
        "127.0.0.1:5173",
        "127.0.0.1:3000",
    ]
    static_dir: str = "static"
    image_dir: str = "static/images"

    class Config:
        env_file = ".env"


settings = Settings()
