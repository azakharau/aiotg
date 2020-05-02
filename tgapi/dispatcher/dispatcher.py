import asyncio
import itertools
import json
from asyncio import (BaseEventLoop,
                     AbstractEventLoop)
from typing import (Union,
                    Iterable,
                    Optional, Coroutine, Any)

from tgapi.bot.base_bot import BaseBot
from tgapi.bot.bot import Bot
from tgapi import tgtypes
from tgapi.exceptions import TelegramAPIException
from .handler import Handler


class Dispatcher:
    """Updates dispatcher

    It will process incoming updates: messages, edited messages (TDD)
    """

    def __init__(self,
                 bot: Bot,
                 loop: Union[BaseEventLoop, AbstractEventLoop] = None,
                 run_by_default: bool = False,
                 filters: Optional[Iterable] = None):

        if not isinstance(bot, BaseBot):
            raise TypeError(f"'bot' parameter must be an instance "
                            f"of Bot object, not {type(bot).__name__}")

        if not loop:
            self._loop = bot.loop

        self._bot = bot
        self._run_by_default = run_by_default
        self._filters = filters if filters else None
        self._update_handler = Handler()
        self._message_handlers = Handler()
        self._polling = None
        self._update_handler.register(self.process_update)

    async def skip_updates(self):
        await self._bot.get_updates(offset=-1, timeout=1)

    async def process_update(self,
                             update: tgtypes.Update) -> \
            list:
        if update.message:
            return await self._message_handlers.notify(
                tgtypes.dataclass_factory(tgtypes.Message, update.message),
                is_message=True)
        if update.edited_message:
            return await self._message_handlers.notify(update.edited_message)

    async def process_updates(self, updates: list):
        tasks = []

        for update in updates:
            tasks.append(self._update_handler.notify(
                update))
        return await asyncio.gather(*tasks)

    async def _process_polling_updates(self, updates: list):
        call = []
        print("updates received")
        for responses in itertools.chain.from_iterable(
                await self.process_updates(updates)):
            for response in responses:
                call.append(response)
        if call:
            try:
                await asyncio.gather(*call)
            except TelegramAPIException:
                ...

    async def start_polling(self,
                            timeout: Optional[int] = 30,
                            relax_timeout: Optional[int] = 0.1,
                            limit: Optional[int] = None):

        if self._polling:
            raise RuntimeError("Long polling is running")

        self._polling = True
        offset = None

        while self._polling:
            try:
                updates = await self._bot.get_updates(offset=offset,
                                                      limit=limit,
                                                      timeout=timeout)
            except asyncio.CancelledError:
                break

            if updates:
                with open('test.json', 'w') as f:
                    json.dump([update.to_dict() for update in updates], f)
                offset = updates[-1].update_id + 1
                self._loop.create_task(self._process_polling_updates(updates))

            if relax_timeout:
                await asyncio.sleep(relax_timeout)

    async def _shutdown(self):
        self._polling = False
        await self._bot.close()

    async def stop_polling(self):
        if hasattr(self, '_polling'):
            self._polling = False

    def register_message_handler(self,
                                 callback,
                                 *filters,
                                 commands):
        """

        Args:
            callback:
            *filters:
            commands:

        Returns:

        """
        self._message_handlers.register(callback, commands)

    def message_handler(self, *filters, commands = None):
        """

        Args:
            *filters:

        Returns:

        """

        def wrapper(callback):
            self.register_message_handler(callback,
                                          *filters,
                                          commands=commands)
            return callback

        return wrapper


    def run(self):
        self._loop.create_task(self.start_polling())
        self._loop.run_forever()