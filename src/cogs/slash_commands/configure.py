from disnake import ApplicationCommandInteraction, TextChannel
from disnake.ext import commands

DESCRIPTION = 'Укажите канал куда будут пересылаться сообщения'


class ConfigureSlashCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(description=DESCRIPTION)
    @commands.has_permissions(administrator=True)
    async def configure(self, inter: ApplicationCommandInteraction, channel: TextChannel):
        await inter.response.send_message(channel.name)


def setup(bot: commands.Bot):
    bot.add_cog(ConfigureSlashCommand(bot))
