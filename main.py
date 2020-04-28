import asyncio
import os

import uvloop

from bot.bot import Bot
from dispatcher.dispatcher import Dispatcher

tasks = []
path = f"{os.getcwd()}/test.json"

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

bot = Bot()

dispatcher = Dispatcher(bot=bot)

@dispatcher.message_handler()
async def test(message):
    await bot.send_message(424177117, "Hello yoba")


@dispatcher.message_handler()
async def ttt(message):
    await bot.send_message(message[0].from_user['id'], "2123")




if __name__ == '__main__':
    dispatcher.run()
