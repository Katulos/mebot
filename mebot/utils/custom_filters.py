from pyrogram import filters


async def _admins(_, __, ___) -> None:
    return filters.user()


admins = filters.create(_admins)
