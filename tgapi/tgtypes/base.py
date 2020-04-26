import dataclasses
import json

import typing
from copy import deepcopy
from pprint import pprint


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

@dataclasses.dataclass()
class BaseDataEntity:

    def to_dict(self) -> dict:
        __data = dataclasses.asdict(self)
        if "from_user" in __data:
            __data['from'] = deepcopy(__data['from_user'])
            del __data['from_user']
        return __data

    def to_json(self) -> json:
        return json.dumps(self.to_dict())

    # def __getattr__(self, item):
    #     ...
    #
    # def __setattr__(self, key, value):
    #     ...
    #
    # def __delattr__(self, item):
    #     ...


def dataclass_factory(cls: dataclasses.dataclass,
                      data: typing.Union[
                          typing.List[dict], dict]) -> dataclasses.dataclass:
    """

    Args:
        cls:
        data:

    Returns:

    """
    if not dataclasses.is_dataclass(cls):
        raise ValueError("cls parameter must be dataclass type")
    if "from" in data:
        data['from_user'] = deepcopy(data['from'])
        del data['from']
    if isinstance(data, list):
        if len(data) == 1:
            _data = data[0]
            return cls(**_data)
        return [cls(**d) for d in data]

    elif isinstance(data, dict):
        return cls(**data)

    else:
        raise ValueError(
            "data parameter could be list of dicts or single dict")
