from __future__ import annotations

import logging

from app.bot.config.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TORTOISE_ORM = {
    "connections": {"default": settings.get("database_url")},
    "apps": {
        "app": {
            "models": ["app.bot.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "use_tz": True,
}
