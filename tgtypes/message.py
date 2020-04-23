import dataclasses

import typing

from tgtypes.chat import Chat
from tgtypes.user import User


@dataclasses.dataclass(frozen=False)
class Message:
    """This object represents a Telegram message."""
    message_id: typing.Optional[int] = None
    from_user: typing.Optional[User] = None
    chat: typing.Optional[Chat] = None
    date: typing.Optional[int] = None
    edit_date: typing.Optional[int] = None
    text: typing.Optional[str] = None
