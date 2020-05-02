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
    await bot.send_message(message[0].from_user['id'], "Hello")

@dispatcher.message_handler(commands=['/hi'])
async def tt(message):
    await bot.send_message(message[0].from_user['id'], "Zdarova")

@dispatcher.message_handler()
async def ttt(message):
    await bot.send_message(424177117, "Hey you")




if __name__ == '__main__':
    dispatcher.run()
