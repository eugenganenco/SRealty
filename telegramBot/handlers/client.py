from aiogram import types, Dispatcher
from telegramBot.main import bot
from telegramBot.keyboards import kb_client
from telegramBot.dataBase import dataBase as db



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


# Команда активации подписки
# @dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_subscriber(message.from_user.id)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, True)

    await message.answer(
        "You have successfully subscribed to the bot")


# Команда отписки
# @dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subscriber(message.from_user.id, False)
        await message.answer("You are already subscribed.")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subscription(message.from_user.id, False)
        await message.answer("You have successfully unsubscribed from the bot")

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_menu, commands=['menu'])
    dp.register_message_handler(subscribe, commands=['subscribe'])
    dp.register_message_handler(unsubscribe, commands=['unsubscribe'])
