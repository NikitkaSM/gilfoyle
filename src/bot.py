from disnake import Intents
from disnake.ext import commands

from src.core.config import SECRET
from src.core.setup import load_cogs
from src.models import db_helper, Base

bot = commands.Bot(intents=Intents.all(), command_prefix='$')

load_cogs(bot)


@bot.event
async def on_ready():
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print(f'{bot.user.name} онлайн!')


bot.run(SECRET)
