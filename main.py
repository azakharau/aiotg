import asyncio
import json
import os
import socket
from pprint import pprint

import aiohttp

import settings
from utils import tg_api


async def main():
    async with aiohttp.TCPConnector(family=socket.AF_INET,
                              ssl=False) as connector:
        async with aiohttp.ClientSession(connector=connector) as session:
            task = tg_api.get_updates(session,
                                      settings.TELEGRAM_API_URL)
            result = await asyncio.gather(task)

            path = f"{os.getcwd()}/test.json"
            if result:
                with open(path, 'w') as f:
                    json.dump(*result, f, indent=2)
            pprint(*result)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())