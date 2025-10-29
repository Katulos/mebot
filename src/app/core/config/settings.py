import logging
import os
from pathlib import Path

from dynaconf import Dynaconf, ValidationError, Validator

_BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent.parent


settings = Dynaconf(
    settings_files=[
        "?/etc/mebot/settings.yml",
        "?/etc/mebot/.secrets.yml",
        "?~/.config/mebot/settings.yml",
        "?~/.config/mebot/.secrets.yml",
        os.path.join(_BASE_DIR, "settings.yml"),
        os.path.join(_BASE_DIR, ".secrets.yml"),
    ],
)

settings.validators.register(
    # Client
    Validator(
        "api_id",
        apply_default_on_none=True,
        default=2040,
        is_type_of=int,
        required=True,
    ),
    Validator(
        "api_hash",
        apply_default_on_none=True,
        default="b18441a1ff607e10a989891a5462e627",
        required=True,
    ),
    Validator(
        "app_version",
        apply_default_on_none=True,
        default="5.12.1 x64",
        required=True,
    ),
    Validator(
        "device_model",
        apply_default_on_none=True,
        default="B75M-D3H-BT",
        required=True,
    ),
    Validator(
        "lang_code",
        apply_default_on_none=True,
        default="en",
        required=True,
    ),
    Validator(
        "system_lang_code",
        apply_default_on_none=True,
        default="en-US",
        required=True,
    ),
    Validator(
        "system_version",
        apply_default_on_none=True,
        default="Windows 10",
        required=True,
    ),
    Validator("bot_token", apply_default_on_none=False),
    Validator("phone", apply_default_on_none=False),
    Validator(
        "admins",
        apply_default_on_none=True,
        default=[],
        is_type_of=list,
        required=True,
    ),
    Validator(
        "session",
        default=os.path.join(_BASE_DIR, "data/session"),
        required=True,
    ),
    # Database
    # like a postgres://postgres:postgres@db:5432/postgres
    Validator(
        "database_url",
        default="sqlite://" + os.path.join(_BASE_DIR, "data/db.sqlite3"),
        required=True,
    ),
    # debug
    Validator("debug", default=False, is_type_of=bool),
)

try:
    settings.validators.validate_all()
except ValidationError as e:
    logging.error(e.message)
