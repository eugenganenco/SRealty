import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from telegramBot.config import API_TOKEN
from aiogram.utils import executor
from telegramBot.config import URL_APP
from telegramBot.handlers import client, other
from telegramBot.dataBase import dataBase

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
db = dataBase.Database()


async def on_startup():
    print('Bot is online')
    await bot.set_webhook(URL_APP)


# don't forget to close the db (cursor and database)
async def on_shutdown():
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