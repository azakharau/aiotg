import dataclasses
import json
from copy import deepcopy


class SingletonMixin:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonMixin, cls).__new__(cls)
        return cls.instance


@dataclasses.dataclass()
class BaseDataEntityMixin:

    def to_dict(self) -> dict:
        __data = dataclasses.asdict(self)
        if "from_user" in __data:
            __data['from'] = deepcopy(__data['from_user'])
            del __data['from_user']
        return __data

    def to_json(self) -> json:
        return json.dumps(self.to_dict())
