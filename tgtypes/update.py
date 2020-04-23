from dataclasses import dataclass

import typing

from tgtypes.message import Message


@dataclass()
class Update:
    update_id: typing.Optional[int] = None
    message: typing.Optional[Message] = None
    edited_message: typing.Optional[Message] = None