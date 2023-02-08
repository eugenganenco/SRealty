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
from apscheduler.schedulers.asyncio import AsyncIOScheduler

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)



async def on_startup(dp):
    print('Bot is online')
    await bot.set_webhook(URL_APP)


# don't forget to close the db (cursor and database)
async def on_shutdown(dp):
    await bot.delete_webhook()
    await db.close()


async def sendNotification():
    now = datetime.utcnow()
    await bot.send_message(db.get_subscriptions(), f"{now}")


client.register_handlers_client(dp)
other.register_handlers_other(dp)

scheduler = AsyncIOScheduler()
scheduler.add_job(sendNotification, 'interval', seconds=10)
scheduler.start()




executor.start_webhook(
    loop=scheduler,
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 500))
)