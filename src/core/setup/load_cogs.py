import os

from disnake.ext.commands import Bot

from src.core.config import get_settings

settings = get_settings()


def load_cogs(bot: Bot):
    cog_directory = "cogs"

    for root, dirs, files in os.walk(cog_directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file).replace("\\", "/")
                extension = path[:-3].replace("/", ".")
                try:
                    bot.load_extension(extension)
                    print(f"Loaded extension: {extension}")
                except Exception as e:
                    print(f"Failed to load extension {extension}: {e}")
