import typing
from dataclasses import dataclass

from tgapi.utils import BaseDataEntityMixin


@dataclass()
class User(BaseDataEntityMixin):
    id: typing.Optional[int] = None
    is_bot: typing.Optional[bool] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: typing.Optional[str] = None
    language_code: typing.Optional[str] = None
