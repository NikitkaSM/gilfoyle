from disnake import Guild
from disnake.ext.commands import Bot

from src.core.config import get_settings

settings = get_settings()


async def log_message(
        bot: Bot,
        guild_id: int = settings.root_guild,
        channel_id: int = settings.root_guild_logs_channel,
        **args
):
    guild: Guild = await bot.fetch_guild(guild_id)
    channel = await guild.fetch_channel(channel_id)
    await channel.send(**args)
