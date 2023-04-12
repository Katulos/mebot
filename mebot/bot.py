from __future__ import annotations

import sys
from functools import partial

from pyrogram import Client, errors, filters
from tortoise import Tortoise

from mebot import TORTOISE_ORM, logger, settings

command = partial(filters.command, prefixes=["!", "/", "."])


class Bot(Client):  # pylint: disable=too-many-ancestors
    def __init__(self):
        if settings.PHONE:
            super().__init__(
                name=settings.SESSION_URL,
                api_id=settings.API_ID,
                api_hash=settings.API_HASH,
                phone_number=settings.PHONE,
                test_mode=settings.TEST_ENV,
                plugins={"root": "mebot.plugins"},
            )
            logger.info("Auth as user")
        elif settings.BOT_TOKEN:
            super().__init__(
                name=settings.SESSION_URL,
                api_id=settings.API_ID,
                api_hash=settings.API_HASH,
                bot_token=settings.BOT_TOKEN,
                test_mode=settings.TEST_ENV,
                plugins={"root": "mebot.plugins"},
            )
            logger.info("Auth as bot")
        else:
            logger.critical(
                "One of the mandatory parameters for authorization"
                " (BOT_TOKEN or PHONE) is not defined",
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
