from aiogram import types, Dispatcher
from telegramBot.create_bot import dp, bot
from telegramBot.keyboards import kb_client

#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.message):
    try:
        await bot.send_message(message.from_user.id, 'Bon appetite', reply_markup=kb_client )
        await message.delete()
    except:
        await message.reply('Communication with the bot through personal chat only:\nhttps://t.me/CzechRealEstateBot')

#@dp.message_handler(commands=['Menu'])
async def commands_menu(message: types.message):
    await bot.send_message(message.from_user.id, 'this is Menu')

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_menu, commands=['menu'])
