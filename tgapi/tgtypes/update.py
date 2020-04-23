import typing
from dataclasses import dataclass

from .message import Message


@dataclass()
class Update:
    update_id: typing.Optional[int] = None
    message: typing.Optional[Message] = None
    edited_message: typing.Optional[Message] = None
