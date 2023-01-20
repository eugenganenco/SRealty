from aiogram.utils import executor
from create_bot import dp


async def on_startup(_):
    print('Bot is online')
    print('Access to data base')

from handlers import client, other

client.register_handlers_client(dp)
other.register_handlers_other(dp)

#when bot online will not respond to queries sent when it was offline
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)