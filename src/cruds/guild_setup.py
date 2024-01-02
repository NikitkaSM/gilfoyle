from sqlalchemy.ext.asyncio import AsyncSession

from src.models import GuildSetup


async def create_guild_setup(session: AsyncSession, sending_channel_id: int, guild_id: int):
    guild_setup = GuildSetup(sending_channel_id=sending_channel_id, guild_id=guild_id)

    session.add(guild_setup)
    await session.commit()
    await session.refresh(guild_setup)

    return guild_setup
