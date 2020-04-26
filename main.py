import asyncio
import dataclasses
import json
import os
import socket
from pprint import pprint

import aiohttp

import settings
from utils.bot_helpers import setup_bot_settings
from tgapi import apimethods
from tgapi.tgtypes import update, base
from tgapi import tgtypes

tasks = []
path = f"{os.getcwd()}/test.json"


def upd(session):
    task = apimethods.get_updates(session,
                                  settings.BOT_URL)
    tasks.append(task)


def del_msg(session):
    with open(path) as f:
        data = json.load(f)
    for dict_ in data:
        if not dict_.get('message'):
            if dict_.get('edited_message'):
                task = apimethods.delete_message(session,
                                                 settings.BOT_URL,
                                                 dict_[
                                                     'edited_message'][
                                                     'chat'][
                                                     'id'],
                                                 dict_[
                                                     'edited_message'][
                                                     'message_id'])
                tasks.append(task)
                continue
            else:
                continue
        task = apimethods.delete_message(session,
                                         settings.BOT_URL,
                                         dict_['message']['chat'][
                                             'id'],
                                         dict_['message'][
                                             'message_id'])
        tasks.append(task)


def send_msg(session):
    task = apimethods.send_message(session,
                                   settings.BOT_URL,
                                   chat_id=settings.BOT_CHAT_ID,
                                   text="Kuku youba!")
    tasks.append(task)

async def main():
    async with aiohttp.TCPConnector(family=socket.AF_INET,
                                    ssl=False) as connector:
        async with aiohttp.ClientSession(connector=connector) as session:
            # tasks.append(setup_bot_settings(session,
            #                                 settings.BOT_URL))
            send_msg(session)
            result: list = await asyncio.gather(*tasks)
    a = tgtypes.base.dataclass_factory(tgtypes.message.Message, *result)
    pprint(a)
    pprint(a.to_dict())
    if result:
        with open(path, 'w') as f:
            json.dump(*result, f, indent=2)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
