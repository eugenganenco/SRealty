import os
from aiogram.utils import executor
from telegramBot.create_bot import dp, bot
from telegramBot.config import URL_APP
from telegramBot.handlers import client, other
from create_bot import cur, base

async def on_startup():
    print('Bot is online')
    await bot.set_webhook(URL_APP)

async def on_shutdown():
    await bot.delete_webhook()
    cur.close()
    base.close()

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