from importlib import reload

import aiohttp

import settings
from tgapi.apimethods import get_me
from tgapi.tgtypes import base, bot_entity


async def setup_bot_settings(session: aiohttp.ClientSession,
                             bot_url: str) -> dict:
    """

    Args:
        session:
        bot_url:

    Returns:

    """
    result = await get_me(session,
                          bot_url)
    bot = base.dataclass_factory(bot_entity.BotEntity, result)
    settings.BOT_ID = bot._id
    settings.BOT_NAME = bot.username
    reload(settings)
    return bot.to_dict()
