from aiogram import types, Dispatcher
from telegramBot.keyboards import kb_client
from telegramBot.dataBase import dataBase as db




#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message: types.message):
    from telegramBot import main
    try:
        await main.bot.send_message(message.from_user.id, 'Bon appetite', reply_markup=kb_client )
        await message.delete()
    except:
        await message.reply('Communication with the bot through personal chat only:\nhttps://t.me/CzechRealEstateBot')

#@dp.message_handler(commands=['Menu'])
async def commands_menu(message: types.message):
    from telegramBot import main
    await main.bot.send_message(message.from_user.id, 'this is Menu')


# @dp.message_handler(commands=['subscribe'])
async def subscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id)
    else:
        db.update_subscription(message.from_user.id, True)

    await message.answer(
        "You have successfully subscribed to the bot")


# @dp.message_handler(commands=['unsubscribe'])
async def unsubscribe(message: types.Message):
    if (not db.subscriber_exists(message.from_user.id)):
        db.add_subscriber(message.from_user.id, False)
        await message.answer("You are already subscribed.")
    else:
        db.update_subscription(message.from_user.id, False)
        await message.answer("You have successfully unsubscribed from the bot")

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_menu, commands=['menu'])
    dp.register_message_handler(subscribe, commands=['subscribe'])
    dp.register_message_handler(unsubscribe, commands=['unsubscribe'])
