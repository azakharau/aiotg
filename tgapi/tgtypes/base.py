import dataclasses

import typing
from copy import deepcopy


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

    if isinstance(data, list):
        if len(data) == 1:
            _data = _prepare_data(data[0])
            return [cls(**_data)]
        return [cls(**_prepare_data(d)) for d in data]

    elif isinstance(data, dict):
        return [cls(**_prepare_data(data))]

    else:
        raise ValueError(
            "data parameter could be list of dicts or single dict")


def _prepare_data(data: dict) -> dict:
    _data = deepcopy(data)

    if "from" in _data:
        _data['from_user'] = deepcopy(data['from'])
        del _data['from']

    return _data

