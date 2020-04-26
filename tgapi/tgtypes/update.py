import typing
from dataclasses import dataclass

from . import base
from .message import Message


@dataclass()
class Update(base.BaseDataEntity):
    update_id: typing.Optional[int] = None
    message: typing.Optional[Message] = None
    edited_message: typing.Optional[Message] = None
