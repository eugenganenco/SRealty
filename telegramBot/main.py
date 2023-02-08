import asyncio
import os
from datetime import datetime

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from telegramBot.config import API_TOKEN
from aiogram.utils import executor
from telegramBot.config import URL_APP
from telegramBot.handlers import client, other
from telegramBot.dataBase import dataBase as db

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)



async def on_startup(dp):
    print('Bot is online')
    await bot.set_webhook(URL_APP)


# don't forget to close the db (cursor and database)
async def on_shutdown(dp):
    await bot.delete_webhook()
    await db.close()


async def sendNotification(frequency):
    while True:
        await asyncio.sleep(frequency)

        now = datetime.utcnow()
        await bot.send_message(db.get_subscriptions(), f"{now}")


client.register_handlers_client(dp)
other.register_handlers_other(dp)

loop = asyncio.get_event_loop()
loop.create_task(sendNotification(10))

executor.start_webhook(
    loop=loop,
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 500))
)