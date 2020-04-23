import asyncio
import dataclasses
import json
import os
import socket
from pprint import pprint

import aiohttp

import settings
from tgapi import apimethods
from tgapi.tgtypes import update

async def main():
    async with aiohttp.TCPConnector(family=socket.AF_INET,
                              ssl=False) as connector:
        async with aiohttp.ClientSession(connector=connector) as session:
            task = apimethods.get_updates(session,
                                          settings.TELEGRAM_API_URL)
            result = await asyncio.gather(task)

            path = f"{os.getcwd()}/test.json"
            if result:
                with open(path, 'w') as f:
                    json.dump(*result, f, indent=2)
            u = [update.Update(**upd) for upd in result[0]]
            pprint([dataclasses.asdict(a) for a in u])

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())