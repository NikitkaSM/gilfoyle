from sqlalchemy.orm import Mapped

from src.models.base import Base


class Connection(Base):
    __tablename__ = 'connections'

    guild_id: Mapped[int]
    connected_guild_id: Mapped[int]
