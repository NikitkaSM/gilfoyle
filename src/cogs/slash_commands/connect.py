from disnake import ApplicationCommandInteraction
from disnake.ext import commands
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Connection

DESCRIPTION = 'Создать соединение с другим сервером'


async def create_connection(session: AsyncSession, guild_id: int, connected_guild_id: int):
    connection = Connection(guild_id=guild_id, connected_guild_id=connected_guild_id)
    session.add(connection)
    await session.commit()
    await session.refresh(connection)

    return connection


class Connect(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description=DESCRIPTION)
    async def connect(self, inter: ApplicationCommandInteraction):
        print(inter.bot.guilds)
        await inter.response.send_message("Connected")


def setup(bot: commands.Bot):
    bot.add_cog(Connect(bot))
