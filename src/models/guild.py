from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base


class Guild(Base):
    __tablename__ = 'guilds'

    id: Mapped[int] = mapped_column(unique=True, primary_key=True)
