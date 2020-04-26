import asyncio
import dataclasses
import json
import os
import socket
from pprint import pprint

import aiohttp

import settings
from tgapi import apimethods
from tgapi.tgtypes import update, base


async def main():
    path = f"{os.getcwd()}/test.json"
    async with aiohttp.TCPConnector(family=socket.AF_INET,
                                    ssl=False) as connector:
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = []
            # task = apimethods.get_updates(session,
            #                               settings.TELEGRAM_API_URL)
            # tasks.append(task)
            with open(path) as f:
                data = json.load(f)
            for dict_ in data:
                if not dict_.get('message'):
                    if dict_.get('edited_message'):
                        task = apimethods.delete_message(session,
                                                         settings.TELEGRAM_API_URL,
                                                         dict_['edited_message'][
                                                             'chat'][
                                                             'id'],
                                                         dict_['edited_message'][
                                                             'message_id'])
                        tasks.append(task)
                        continue
                    else:
                        continue
                task = apimethods.delete_message(session,
                                                 settings.TELEGRAM_API_URL,
                                                 dict_['message']['chat'][
                                                     'id'],
                                                 dict_['message'][
                                                     'message_id'])
                tasks.append(task)
            result: list = await asyncio.gather(*tasks)
            pprint(result)
    if result:
        with open(path, 'w') as f:
            json.dump(*result, f, indent=2)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
