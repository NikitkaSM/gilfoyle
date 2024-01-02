from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Guild


async def create_guild(session: AsyncSession, guild_id: int):
    guild = Guild(id=guild_id)
    session.add(guild)
    await session.commit()
    await session.refresh(guild)

    return guild


async def get_guild(session: AsyncSession, guild_id: int):
    return await session.get(Guild, guild_id)


async def delete_guild(session: AsyncSession, guild: Guild):
    await session.delete(guild)
    await session.commit()
