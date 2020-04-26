import dataclasses
import json

import typing
from pprint import pprint


@dataclasses.dataclass()
class BaseDataEntity:

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)

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
    if not dataclasses.is_dataclass(cls):
        raise ValueError("cls parameter must be dataclass")

    if isinstance(data, list):
        if len(data) == 1:
            _data = data[0]
            return cls(**_data)
        return [cls(**d) for d  in data.pop()]

    elif isinstance(data, dict):
        return cls(**data)

    else:
        raise ValueError(
            "data parameter could be list of dicts or single dict")
