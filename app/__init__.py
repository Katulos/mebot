from __future__ import annotations

import logging
import os.path
from pathlib import Path

import dotenv

from .config import shared

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load env variables from file
dotenv_file = Path(__file__).resolve().parent.parent / ".env"
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

TORTOISE_ORM = {
    "connections": {"default": shared.settings.DATABASE_URL},
    "apps": {
        "app": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
}
