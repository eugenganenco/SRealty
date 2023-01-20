from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from Token import Token
# stores data in memory
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(Token().getToken())
dp = Dispatcher(bot, storage=storage)
print('bot created in create_bot')
