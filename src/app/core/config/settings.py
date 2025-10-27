import logging
import os
import sys
from pathlib import Path

from dynaconf import Dynaconf, ValidationError, Validator

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


settings = Dynaconf(
    settings_files=[
        "?/etc/mebot/settings.yml",
        "?/etc/mebot/.secrets.yml",
        "?~/.config/mebot/settings.yml",
        "?~/.config/mebot/.secrets.yml",
        os.path.join(BASE_DIR, "settings.yml"),
        os.path.join(BASE_DIR, ".secrets.yml"),
    ],
)

settings.validators.register(
    # Pyrogram
    Validator(
        "api_id",
        apply_default_on_none=True,
        default=21724,
        is_type_of=int,
        required=True,
    ),
    Validator(
        "api_hash",
        apply_default_on_none=True,
        default="3e0cb5efcd52300aec5994fdfc5bdc16",
        required=True,
    ),
    Validator("bot_token", apply_default_on_none=False),
    Validator("phone", apply_default_on_none=False),
    Validator(
        "session_url",
        default=os.path.join(BASE_DIR, "data/session"),
        required=True,
    ),
    Validator("test_env", default=False, is_type_of=bool),
    # Database
    # like a postgres://postgres:postgres@db:5432/postgres
    Validator(
        "database_url",
        default="sqlite://" + os.path.join(BASE_DIR, "data/db.sqlite3"),
        required=True,
    ),
    # Antiflood
    Validator("messages", default=3, is_type_of=int, required=True),
    Validator("seconds", default=15, is_type_of=int, required=True),
    Validator("cb_seconds", default=15, is_type_of=int, required=True),
    # debug
    Validator("debug", default=False, is_type_of=bool),
)

try:
    settings.validators.validate_all()
except ValidationError as e:
    logging.error(e.message)
    sys.exit(1)
