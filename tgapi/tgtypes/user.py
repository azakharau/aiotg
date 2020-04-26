import typing
from dataclasses import dataclass

from . import base

@dataclass()
class User(base.BaseDataEntity):
    id: typing.Optional[int] = None
    is_bot: typing.Optional[bool] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: typing.Optional[str] = None
    language_code: typing.Optional[str] = None
