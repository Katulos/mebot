from __future__ import annotations

import asyncio

import tortoise
from pyrogram import enums, errors

from app.bot import logger
from app.bot.models import Chat, ChatMember


async def update_chat_member(chat_id: int, user_id: int, **kwargs):
    """update chat member"""

    await ChatMember.update_or_create(
        chat_id=chat_id,
        user_id=user_id,
        defaults=kwargs,
    )


async def reload_admins(client, chat_id):
    """reload admins"""
    await ChatMember.filter(chat_id=chat_id, is_admin=True).update(
        is_admin=False,
    )
    try:
        participants = []
        async for m in client.get_chat_members(
            chat_id=chat_id,
            filter=enums.ChatMembersFilter.ADMINISTRATORS,
        ):
            participants.append(m)
        for participant in participants:
            if not participant.user.is_deleted:
                await update_chat_member(
                    chat_id,
                    participant.user.id,
                    is_admin=participant.privileges.can_restrict_members,
                    is_bot=participant.user.is_bot,
                    is_deleted=participant.user.is_deleted,
                )
                await Chat.filter(id=chat_id).update(
                    last_admins_update=tortoise.timezone.now(),
                )
    except errors.FloodWait as e:
        logger.error(e.MESSAGE)
        await asyncio.sleep(e.value)
