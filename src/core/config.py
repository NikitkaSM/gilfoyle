import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

SECRET = os.getenv('SECRET')
CLIENT = os.getenv('CLIENT')


class Settings(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///../db.sqlite3'
    db_echo: bool = True
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    root_guild: int = 1096868678244499578
    root_guild_logs_channel: int = 1191393627793010688


def get_settings():
    return Settings()
