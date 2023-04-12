import re

from pyrogram import Client, errors, filters
from pyrogram.types import Message

from mebot import logger
from mebot.bot import command

me_command = "me"


# pylint: disable=no-member
@Client.on_message(
    command([me_command]) & filters.group,
)
async def me_command_handler(client: Client, message: Message) -> None:
    pattern = rf"(?i)^[/!\\.]{me_command} (.*?)$"
    if re.match(pattern, message.text):
        try:
            s = message.text[4:]
            await message.delete()
            await client.send_message(
                message.chat.id,
                f"* <b>{message.from_user.mention}</b> {s}",
                reply_to_message_id=message.reply_to_message_id,
            )
        except errors.MessageDeleteForbidden as e:
            logger.error(e.MESSAGE)
