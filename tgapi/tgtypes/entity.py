import dataclasses
import typing

from tgapi.utils import BaseDataEntityMixin


@dataclasses.dataclass(frozen=False)
class Entity(BaseDataEntityMixin):
    offset: typing.Optional[int] = None
    length: typing.Optional[int] = None
    type: typing.Optional[str] = None
