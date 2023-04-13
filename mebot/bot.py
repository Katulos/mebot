from __future__ import annotations

import sys
from functools import partial

from pyrogram import Client, errors, filters
from tortoise import Tortoise

from mebot import TORTOISE_ORM, logger, settings

command = partial(filters.command, prefixes=["!", "/", "."])


class Bot(Client):  # pylint: disable=too-many-ancestors
    def __init__(self):
        if settings.get("phone"):
            super().__init__(
                name=settings.get("session_url"),
                api_id=settings.get("api_id"),
                api_hash=settings.get("api_hash"),
                phone_number=settings.get("phone"),
                test_mode=settings.get("test_env"),
                plugins={"root": "mebot.plugins"},
            )
            logger.info("Auth as user")
        elif settings.get("bot_token"):
            super().__init__(
                name=settings.get("session_url"),
                api_id=settings.get("api_id"),
                api_hash=settings.get("api_hash"),
                bot_token=settings.get("bot_token"),
                test_mode=settings.get("test_env"),
                plugins={"root": "mebot.plugins"},
            )
            logger.info("Auth as bot")
        else:
            logger.critical(
                "One of the mandatory parameters for authorization"
                " (bot_token or phone) is not defined",
            )
            sys.exit(1)

    async def start(self):
        try:
            await Tortoise.init(config=TORTOISE_ORM)
            await super().start()  # pylint: disable=no-member
        except errors.ApiIdInvalid as e:
            logger.critical(e.MESSAGE)
            sys.exit(1)
        except errors.AccessTokenInvalid as e:
            logger.critical(e.MESSAGE)
            sys.exit(1)
        except errors.PhoneNumberInvalid as e:
            logger.critical(e.MESSAGE)
            sys.exit(1)

    async def stop(self):
        await Tortoise.close_connections()
        await super().stop()  # pylint: disable=no-member
