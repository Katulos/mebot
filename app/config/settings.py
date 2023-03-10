import os
from pathlib import Path
from typing import Optional

from pydantic import BaseSettings, Field

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    DEBUG: bool = Field(default=False, env="DEBUG")

    # Pyrogram
    API_ID: int = Field(env="API_ID")
    API_HASH: str = Field(env="API_HASH")
    # pylint: disable=consider-alternative-union-syntax
    BOT_TOKEN: Optional[str] = Field(
        env="BOT_TOKEN",
    )
    # pylint: disable=consider-alternative-union-syntax
    PHONE: Optional[str] = Field(
        env="PHONE",
    )
    SESSION_URL: str = Field(
        default=os.path.join(BASE_DIR, "data/session"),
        env="SESSION_URL",
    )
    TEST_ENV: bool = Field(default=False, env="TEST_ENV")

    # Antiflood
    MESSAGES = Field(3)
    # Rate limit (N) messages every x seconds
    SECONDS = Field(15)
    # Rate limit x messages every (N) seconds
    CB_SECONDS = Field(15)
    # Rate limit x callback queries every (N) seconds

    # Database
    DATABASE_URL: str = Field(
        default="sqlite://" + os.path.join(BASE_DIR, "data/db.sqlite3"),
        env="DATABASE_URL",
    )

    class Config:
        case_sensitive: bool = True
        env_file = (
            ".env",
            ".env.prod",
            ".env.production",
            ".env.dev",
            ".env.develop",
        )
        env_file_encoding = "utf-8"
        fields = {
            x[0]: {"env": x}
            for x in (
                ["API_ID"],
                ["API_HASH"],
                ["BOT_TOKEN"],
                ["PHONE"],
                ["SESSION_URL"],
                ["TEST_ENV"],
                ["SECONDS"],
                ["CB_SECONDS"],
                ["DATABASE_URL"],
            )
        }
