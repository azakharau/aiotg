import dataclasses

from .base import Singleton, BaseDataEntity

@dataclasses.dataclass()
class BotEntity(Singleton, BaseDataEntity):
    id: int
    is_bot: bool
    first_name: str
    username: str
    supports_inline_queries: bool
    can_join_groups: bool
    can_read_all_group_messages: bool