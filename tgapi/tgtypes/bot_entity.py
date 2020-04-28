import dataclasses

from utils.mixins import BaseDataEntityMixin, SingletonMixin


@dataclasses.dataclass()
class BotEntity(SingletonMixin, BaseDataEntityMixin):
    id: int
    is_bot: bool
    first_name: str
    username: str
    supports_inline_queries: bool
    can_join_groups: bool
    can_read_all_group_messages: bool
