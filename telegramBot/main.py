import asyncio
import os
from datetime import datetime

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
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
    while True:
        now = datetime.utcnow()
        subscribers = db.get_subscriptions()
        for subscriber in subscribers:
            await bot.send_message(subscriber, f"{now}")
        await asyncio.sleep(8)


async def on_shutdown(dp):
    await bot.delete_webhook()
    await db.close()

client.register_handlers_client(dp)
other.register_handlers_other(dp)


executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 500))
)