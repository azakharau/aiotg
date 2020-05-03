import dataclasses
import typing

from tgapi.utils import BaseDataEntityMixin
from .chat import Chat
from .entity import Entity
from .user import User


@dataclasses.dataclass(frozen=False)
class Message(BaseDataEntityMixin):
    """This object represents a Telegram message."""
    message_id: typing.Optional[int] = None
    from_user: typing.Optional[User] = None
    chat: typing.Optional[Chat] = None
    date: typing.Optional[int] = None
    edit_date: typing.Optional[int] = None
    text: typing.Optional[str] = None
    reply_to_message: typing.Optional[int] = None
    entities: typing.Optional[Entity] = None
