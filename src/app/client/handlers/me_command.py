import logging

from telethon.errors import (
    MessageDeleteForbiddenError,
)
from telethon.tl.custom import Message
from telethon.tl.types import User

from app.adapters.db.models import Chat
from app.client.decorators import admin_command, par_command


@par_command("me")
async def me_command(event: Message):
    chat = (
        await Chat.filter(chat_id=event.chat.id)
        .prefetch_related("flags")
        .get_or_none()
    )
    if not chat.flags.enabled:
        return
    try:
        await event.delete()
    except MessageDeleteForbiddenError:
        logging.warning("Grant permission can_delete_messages!")

    sender = await event.get_sender()
    s = event.text[4:]
    if sender is None:
        await event.respond(
            f"*** Some faggot with a crooked nickname {s} ***",
        )
    else:
        await event.respond(f"*** {_get_mention(sender)} {s} ***")


@admin_command("enme")
async def enable_me_command(event: Message):
    chat = (
        await Chat.filter(chat_id=event.chat.id)
        .prefetch_related("flags")
        .get_or_none()
    )
    chat.flags.enabled = True
    await chat.flags.save()
    logging.info(
        f"Enabled /me command in chat ID[{event.chat.id}]: {event.chat.title}",
    )


@admin_command("disme")
async def disable_me_command(event: Message):
    chat = (
        await Chat.filter(chat_id=event.chat.id)
        .prefetch_related("flags")
        .get_or_none()
    )
    chat.flags.enabled = False
    await chat.flags.save()
    logging.info(
        f"Disabled /me command in chat ID[{event.chat.id}]: {event.chat.title}",
    )


def _get_mention(user: User):
    name = user.first_name
    if user.last_name:
        name += " " + user.last_name
    return f"[{name}](tg://user?id={user.id})"
