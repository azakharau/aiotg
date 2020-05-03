import asyncio
import os

import uvloop

from tgapi.bot.bot import Bot
from tgapi.dispatcher.dispatcher import Dispatcher

tasks = []
path = f"{os.getcwd()}/test.json"

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

bot = Bot()

dispatcher = Dispatcher(bot=bot)

@dispatcher.message_handler(commands=['/hello'])
async def t(message):
    await bot.send_message(message.from_user['id'],
                           f"Hello, {message.from_user['first_name']}")

@dispatcher.message_handler(lambda msg: msg.lower().startswith('privet'))
async def tt(message):
    await bot.send_message(message.from_user['id'], "Hi")

@dispatcher.message_handler()
async def ttt(message):
    await bot.send_message(424177117, "anon")




if __name__ == '__main__':
    dispatcher.run()
