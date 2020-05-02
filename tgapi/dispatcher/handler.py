import dataclasses
from typing import List, Optional

from tgapi import exceptions
from tgapi.utils import mixins


class Handler:
    def __init__(self):
        """

        Args:
            dispatcher:
        """
        self.handlers: List[HandlerObject] = []

    def register(self,
                 handler: 'HandlerObject.handler',
                 commands: Optional[list] = None,
                 position: Optional[int] = None) -> bool:
        """

        Args:
            handler:
            position:

        Returns:

        """
        if commands:
            _handler = HandlerObject(handler=handler,
                                     filters=FilterObject(commands=commands))
        else:
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

    async def notify(self, *args, is_message: Optional[bool] = False) -> list:
        """

        Args:
            *args:

        Returns:

        """
        results = []
        for handler_obj in self.handlers:

            try:
                if is_message:
                    response = await self.check_filters(handler_obj,
                                                        *args)
                else:
                    response = await handler_obj.handler(*args)

                if response:
                    results.append(response)

            except exceptions.HandlerCloseException:
                break

        return results

    async def check_filters(self,
                            handler: 'HandlerObject',
                            object: list) -> Optional[callable]:
        """
        Check if handler had an filter.
        If handler has it and it's a bot command -> awaited handler.
        If handler has no filters -> await handlers without filters.
        Else return None
        Args:
            handler:
            object:

        Returns:

        """
        if object[0].entities is None and handler.filters is None:
            return await handler.handler(object)
        elif object[0].entities is None and handler.filters:
            return None
        elif object[0].entities[0]['type'] == "bot_command" \
                and handler.filters:
            if object[0].text in handler.filters.commands:
                return await handler.handler(object)
        return None


@dataclasses.dataclass()
class HandlerObject(mixins.BaseDataEntityMixin):
    handler: callable
    filters: Optional['FilterObject'] = None


@dataclasses.dataclass()
class FilterObject(mixins.BaseDataEntityMixin):
    commands: Optional[list] = None
