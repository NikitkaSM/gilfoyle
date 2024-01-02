from disnake import ApplicationCommandInteraction
from disnake.ext import commands

from disnake.ext.commands.errors import MissingPermissions


class SlashCommandErrorListener(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter: ApplicationCommandInteraction, error: commands.CommandError):
        if isinstance(error, MissingPermissions):
            await inter.response.send_message(
                f'У вас недостаточно прав для использования команды /{inter.application_command.name} :)',
                ephemeral=True)

        await inter.response.send_message(
            'Упс.. Что-то пошло не так, попробуйте использовать команду позже',
            ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(SlashCommandErrorListener(bot))
