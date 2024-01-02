from disnake import Guild
from disnake.ext import commands
from disnake.ext.commands import Bot

from src.cruds.guild import delete_guild, get_guild
from src.models import db_helper
from src.utils import log_message


class GuildLeaveListener(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_remove(self, guild: Guild):
        session = await db_helper.get_scoped_session()

        await delete_guild(session, await get_guild(session, guild.id))

        await log_message(self.bot, content=f'Бот покинул сервер {guild.name}, ID {guild.id}')


def setup(bot: Bot):
    bot.add_cog(GuildLeaveListener(bot))
