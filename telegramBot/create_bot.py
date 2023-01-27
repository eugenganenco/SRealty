import os
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from telegramBot.config import API_TOKEN
# stores data in memory
import psycopg2 as ps

base = ps.connect(os.environ.get('DATABASE_URL'), sslmode='require')
cur = base.cursor()
storage = MemoryStorage()

bot = Bot(API_TOKEN)
dp = Dispatcher(bot, storage=storage)
print('bot created in create_bot')
