from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base


class GuildSetup(Base):
    __tablename__ = 'guild_setups'

    sending_channel_id: Mapped[int] = mapped_column(unique=True)
    guild_id = mapped_column(ForeignKey('connections.id'))
