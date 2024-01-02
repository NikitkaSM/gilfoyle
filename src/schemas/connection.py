from pydantic import BaseModel, ConfigDict


class ConnectionBase(BaseModel):
    guild_id: int
    connected_guild: int


class Connection(ConnectionBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
