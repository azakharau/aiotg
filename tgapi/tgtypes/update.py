import typing
from dataclasses import dataclass

from tgapi.utils import BaseDataEntityMixin
from .message import Message


@dataclass()
class Update(BaseDataEntityMixin):
    update_id: typing.Optional[int] = None
    message: typing.Optional[Message] = None
    edited_message: typing.Optional[Message] = None
