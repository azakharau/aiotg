import typing
from dataclasses import dataclass

from utils.mixins import BaseDataEntityMixin


@dataclass()
class Chat(BaseDataEntityMixin):
    id: typing.Optional[int] = None
    type: typing.Optional[str] = None
    username: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
