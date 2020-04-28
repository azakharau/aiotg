import dataclasses
from typing import List, Optional

from tgapi import exceptions
from utils import mixins


class Handler:
    def __init__(self):
        """

        Args:
            dispatcher:
        """
        self.handlers: List[HandlerObject] = []

    def register(self,
                 handler: 'HandlerObject.handler',
                 position: Optional[int] = None) -> bool:
        """

        Args:
            handler:
            position:

        Returns:

        """
        _handler = HandlerObject(handler=handler)

        if position is None:
            self.handlers.append(_handler)
        else:
            self.handlers.insert(position, _handler)

        return True

    def unregister(self, handler: 'Handler') -> bool:
        """

        Args:
            handler:

        Returns:

        """
        for handler_obj in self.handlers:
            registered = handler_obj.handler
            if handler is registered:
                self.handlers.remove(handler_obj)
                return True
        return False

    async def notify(self, *args):
        """

        Args:
            *args:

        Returns:

        """
        results = []
        for handler_obj in self.handlers:
            try:
                response = await handler_obj.handler(*args)

                if response:
                    results.append(response)

            except exceptions.HandlerCloseException:
                break

        return results


@dataclasses.dataclass()
class HandlerObject(mixins.BaseDataEntityMixin):
    handler: callable
    filters : Optional[list] = None
