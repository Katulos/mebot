import os
import sys
from pathlib import Path

from dynaconf import Dynaconf, ValidationError, Validator

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEFAULT_CONFIG_PATH: str = os.pathsep.join(
    [
        "?/etc/mebot/settings.toml",
        "?/etc/mebot/.secrets.toml",
        "?~/.config/mebot/settings.toml",
        "?~/.config/mebot/.secrets.toml",
        os.path.join(BASE_DIR, "settings.toml"),
        os.path.join(BASE_DIR, ".secrets.toml"),
    ],
)

settings = Dynaconf(
    settings_files=DEFAULT_CONFIG_PATH,
)

settings.validators.register(
    # Pyrogram
    Validator(
        "api_id",
        apply_default_on_none=False,
        is_type_of=int,
        required=True,
    ),
    Validator("api_hash", apply_default_on_none=False, required=True),
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
    accumulative_errors = e.message
    print(accumulative_errors)
    sys.exit(1)
