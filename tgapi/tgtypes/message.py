import dataclasses
import typing

from . import base
from .chat import Chat
from .user import User


@dataclasses.dataclass(frozen=False)
class Message(base.BaseDataEntity):
    """This object represents a Telegram message."""
    message_id: typing.Optional[int] = None
    from_user: typing.Optional[User] = None
    chat: typing.Optional[Chat] = None
    date: typing.Optional[int] = None
    edit_date: typing.Optional[int] = None
    text: typing.Optional[str] = None
