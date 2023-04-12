from __future__ import annotations

import logging
import sys

from pydantic import ValidationError

from mebot.config import Settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    settings = Settings()
except ValidationError as e:
    logger.critical(e)
    sys.exit(0)


TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "mebot": {
            "models": ["mebot.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
}
