import dataclasses
import logging
from typing import List, Optional, Tuple

from tgapi import exceptions, tgtypes
from tgapi.utils import mixins

log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)


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
                 *filters) -> bool:
        """

        Args:
            handler:
            commands:
            *filters:

        Returns:

        """

        if filters and commands:
            _handler = HandlerObject(handler=handler,
                                     filters=FilterObject(commands=commands,
                                                          custom=
                                                          list(filters)))
        elif filters:
            _handler = HandlerObject(handler=handler,
                                     filters=FilterObject(custom=
                                                          list(filters)))
        elif commands:
            _handler = HandlerObject(handler=handler,
                                     filters=FilterObject(commands=commands))
        else:
            _handler = HandlerObject(handler=handler)

        self.handlers.append(_handler)

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
                    response = await self._check_filters(handler_obj,
                                                         *args)
                else:
                    response = await handler_obj.handler(*args)

                if response:
                    results.append(response)

            except exceptions.HandlerCloseException:
                break

        return results

    async def _check_filters(self,
                             handler: 'HandlerObject',
                             object: List[tgtypes.Message]) -> \
            Optional[callable]:
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
        _filters_spec = (False, False)

        if handler.filters is None:
            log.debug(f"not handler.filters.commands and "
                      f"not handler.filters.custom at {handler.handler.__name__}")
            return await handler.handler(*object)

        else:
            _filters_spec: tuple = handler.filters.get_filters_spec()  # (commands: bool, custom: bool)
            log.debug(f"{handler.handler.__name__}, {_filters_spec}")

        if all(_filters_spec):
            log.debug("handler.filters.commands and handler.filters.custom")
            if self._check_custom_filters(handler, *object) and \
                    self._check_bot_commands(handler, *object):
                return await handler.handler(*object)

            return None

        elif _filters_spec[1] and not _filters_spec[0]:
            log.debug(
                "handler.filters.custom and not handler.filters.commands")
            if self._check_custom_filters(handler, *object):
                return await handler.handler(*object)

            return None

        elif _filters_spec[0] and not _filters_spec[1]:
            log.debug(
                "handler.filters.commands and not handler.filters.custom")
            if self._check_bot_commands(handler, *object):
                return await handler.handler(*object)

            return None

    def _check_custom_filters(self,
                              handler: 'HandlerObject',
                              object) -> bool:

        if len(handler.filters.custom) > 1:
            _result = []
            for filter in handler.filters.custom:
                if filter(object.text):
                    _result.append(True)
                continue
            if all(_result):
                return True
        else:
            if handler.filters.custom[0](object.text):
                return True
        return False

    def _check_bot_commands(self,
                            handler: 'HandlerObject',
                            object) -> bool:

        if object.entities is None:
            return False

        if object.entities[0]['type'] == "bot_command":
            if object.text in handler.filters.commands:
                return True
        return False


@dataclasses.dataclass()
class HandlerObject(mixins.BaseDataEntityMixin):
    handler: callable
    filters: Optional['FilterObject'] = None


@dataclasses.dataclass()
class FilterObject(mixins.BaseDataEntityMixin):
    commands: Optional[list] = None
    custom: Optional[list] = None

    def get_filters_spec(self) -> Tuple[bool]:
        _result = []

        if self.commands is None:
            _result.append(False)
        else:
            _result.append(True)

        if self.custom is None:
            _result.append(False)
        else:
            _result.append(True)

        return tuple(_result)
