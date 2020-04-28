import json
import ssl
from asyncio import (BaseEventLoop,
                     AbstractEventLoop,
                     get_event_loop,
                     new_event_loop)
from typing import (Optional,
                    Union)

import aiohttp
import certifi

import settings
from utils.mixins import SingletonMixin


class BaseBot(SingletonMixin):
    def __init__(self,
                 token: Optional[str] = None,
                 loop: Union[BaseEventLoop, AbstractEventLoop] = None,
                 connections_limit: Optional[int] = None,
                 timeout:\
                 Optional[Union[int, float, aiohttp.ClientTimeout]] = None):
        """
        
        Args:
            token: Bot token from @BotFather.
            loop: asyncio event loop.
            connections_limit: connections limit for aiohttp.ClientSession
            timeout: Request timeout.
        """

        self._token = token if token else settings.BOT_TOKEN
        if not self.token:
            raise Exception("Bot token must be set up as bot parameter"
                            "in setting.BOT_TOKEN or "
                            "as environment variable")
        self._id = int(self.token.split(sep=':')[0])
        if not loop:
            self._loop = get_event_loop()
        ssl_context = ssl.create_default_context(cafile=certifi.where())

        self._connector = aiohttp.TCPConnector(limit=connections_limit,
                                               ssl=ssl_context,
                                               loop=self._loop)
        self._timeout = timeout if timeout else settings.DEFAULT_TIMEOUT
        self._session = aiohttp.ClientSession(connector=self._connector,
                                              loop=self._loop,
                                              json_serialize=json.dumps)
        self._url = settings.BOT_URL if settings.BOT_URL else \
            f'https://api.telegram.org/bot{self._token}'

    async def close(self) -> None:
        """
        Close aiohttp.ClienSession
        Returns: None

        """
        await self.session.close()

    def __del__(self):
        if not hasattr(self, '_loop') or not hasattr(self, '_session'):
            return
        if self._loop.is_running():
            self._loop.create_task(self.close())
            return
        loop = new_event_loop()
        loop.run_until_complete(self.close())

    @property
    def token(self):
        """
        Alias for bot token.

        Returns: bot token.

        """
        return self._token

    @property
    def loop(self):
        """
        Alias for bot event loop.

        Returns: asyncio.BaseEventLoop object.

        """
        return self._loop

    @property
    def connector(self):
        """
        Alias for aiohttp.TCPConnector

        Returns: aiohttp.Connector object.

        """
        return self._connector

    @property
    def url(self):
        """
        Alias for default bot request URL.

        Returns: request URL.

        """
        return self._url

    @property
    def session(self):
        """
        Alias for aiohttp.ClientSession

        Returns: aiohttp.ClientSession object.

        """
        return self._session
