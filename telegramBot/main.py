import os

from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from telegramBot.create_bot import dp, bot
from telegramBot.Token import Token
from create_bot import cur, base

async def on_startup(dp):
    print('Bot is online')
    await bot.set_webhook(Token().getUrl())

async def on_shutdown(dp):
    await bot.delete_webhook()
    cur.close()
    base.close()

from telegramBot.handlers import client, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)

#when bot online will not respond to queries sent when it was offline
executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 500))
)