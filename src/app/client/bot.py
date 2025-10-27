from __future__ import annotations

import logging
import sys
from functools import partial

from pyrogram import Client, errors, filters
from tortoise import Tortoise

from app.adapters.db import TORTOISE_ORM
from app.core.config import settings

command = partial(filters.command, prefixes=["!", "/", "."])


class Bot(Client):
    def __init__(self):
        if settings.get("phone"):
            super().__init__(
                name=settings.get("session_url"),
                api_id=settings.get("api_id"),
                api_hash=settings.get("api_hash"),
                phone_number=settings.get("phone"),
                test_mode=settings.get("test_env"),
                plugins={"root": "app.bot.plugins"},
            )
            logging.info("Auth as user")
        elif settings.get("bot_token"):
            super().__init__(
                name=settings.get("session_url"),
                api_id=settings.get("api_id"),
                api_hash=settings.get("api_hash"),
                bot_token=settings.get("bot_token"),
                test_mode=settings.get("test_env"),
                plugins={"root": "app.bot.plugins"},
            )
            logging.info("Auth as bot")
        else:
            logging.critical(
                "One of the mandatory parameters for authorization"
                " (bot_token or phone) is not defined",
            )
            sys.exit(1)

    async def start(self):
        try:
            await Tortoise.init(config=TORTOISE_ORM)
            await super().start()
        except errors.ApiIdInvalid as e:
            logging.critical(e.MESSAGE)
            sys.exit(1)
        except errors.AccessTokenInvalid as e:
            logging.critical(e.MESSAGE)
            sys.exit(1)
        except errors.PhoneNumberInvalid as e:
            logging.critical(e.MESSAGE)
            sys.exit(1)

    async def stop(self):
        await Tortoise.close_connections()
        await super().stop()
