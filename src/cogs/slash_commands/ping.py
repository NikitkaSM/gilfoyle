from disnake import ApplicationCommandInteraction
from disnake.ext import commands


class PingCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command()
    async def ping(self, inter: ApplicationCommandInteraction):
        await inter.response.send_message(f"Тут должна быть задержка между сервером и клиентом..")


def setup(bot: commands.Bot):
    bot.add_cog(PingCommand(bot))
