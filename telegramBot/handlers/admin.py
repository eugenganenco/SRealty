from aiogram import Dispatcher
from aiogram import types
import os

ADMIN_ID = 1292563841

async def on_file_received(message: types.Message):
    # Check if the sender is an admin of the bot
    if message.from_user.id != ADMIN_ID:
        await message.reply('This function is not available for you.')
        return

    # Get the file id from the message
    file = message.document
    file_id = file.file_id

    # Use the aiogram bot to download the file
    from telegramBot import main
    async with main.bot.api.get_file(file_id) as resp:
        file_data = await resp.read()

    # Save the file in the desired location
    path = os.path.join('..', 'newHouses.csv')
    with open(path, 'wb') as f:
        f.write(file_data)

    # Notify the users about the new properties on the market
    main.bot.notify()


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(on_file_received, content_types=types.ContentType.DOCUMENT)