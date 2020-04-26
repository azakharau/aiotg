import typing
from dataclasses import dataclass

from . import base

@dataclass()
class Chat(base.BaseDataEntity):
    id: typing.Optional[int] = None
    type: typing.Optional[str] = None
    username: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
