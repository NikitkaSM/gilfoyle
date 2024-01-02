from disnake import Guild
from disnake.ext import commands

from src.cruds.guild import create_guild
from src.models import db_helper
from src.utils import log_message


class GuildJoinListener(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild: Guild):
        session = await db_helper.get_scoped_session()

        await create_guild(session, guild.id)
        await log_message(bot=self.bot, content=f'Бот зашел на сервер {guild.name}, ID {guild.id}')


def setup(bot: commands.Bot):
    bot.add_cog(GuildJoinListener(bot))
