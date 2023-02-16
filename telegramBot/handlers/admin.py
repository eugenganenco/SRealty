from aiogram import Dispatcher
from aiogram import types
import os
import io
import logging
import pandas as pd

ADMIN_ID = 1292563841


async def on_file_received(message: types.Message):
    # Check if the sender is an admin of the bot
    if message.from_user.id != ADMIN_ID:
        await message.reply('This function is not available for you.')
        return

    # Get the file id from the message
    file_id = message.document.file_id

    # Use the aiogram bot to download the file
    from telegramBot import main
    async with main.bot.get_file(file_id) as resp:
        file_data = await resp.read()

    # Save the file in the desired location
    path = os.path.join('..', 'newHouses.csv')
    with open(path, 'wb') as f:
        f.write(file_data)

    # Notify the users about the new properties on the market
    main.bot.notify()


async def on_file_received2(message: types.Message):
    file_id = message.document.file_id
    from telegramBot import main
    file = await main.bot.download_file_by_id(file_id)
    file_path = os.path.join('..', 'newHouses.csv')
    with open(file_path, 'wb') as f:
        f.write(file)
    await main.bot.send_message(chat_id=message.chat.id, text='CSV file has been saved.')
    main.bot.notify()


async def on_file_received3(message: types.Message):
    # Download the csv file from admin
    file_id = message.document.file_id
    from telegramBot import main
    file = await main.bot.download_file_by_id(file_id)

    # Create a dataframe from csv
    #df = pd.read_csv(io.StringIO(file.decode('utf-8')).getvalue())
    df = pd.read_csv(file, encoding='iso-8859-1')

    # Clean column names and map the 'pandas' data types to sql data types
    # Force column names to be lower case, no spaces, no dashes
    df.columns = [x.lower().replace(" ", "_").replace("-", "_").replace(r"/", "_") \
                      .replace("\\", "_").replace(".", "_").replace("$", "").replace("%", "") for x in df.columns]

    # Dictionary that maps pandas data types to sql datatypes
    replacements = {
        'timedelta64[ns]': 'varchar',
        'object': 'varchar',
        'float64': 'float',
        'int64': 'int',
        'datetime64': 'timestamp'
    }

    # String that will be used to create the sql table
    columnString = ", ".join(
        "{} {}".format(n, d) for (n, d) in zip(df.columns, df.dtypes.replace(replacements)))

    # Create SQL table
    main.db.create_table("uploadedproperties", columnString)

    # Upload the cvs file data to the sql database
    main.db.uploadCSV(file, "uploadedproperties")

    # Confirm that the file was uploaded to the database
    await main.bot.send_message(chat_id=message.chat.id, text='CSV file has been saved.')

    # Send recommendation to the subscribers based on the new properties uploaded
    main.bot.notify()


# Get data in csv form
# Create a dataframe from csv
# Clean col names
# Create SQL table with df.col() as column names and name 'uploaded files'
# Save df to csv
# Open the csv file, save it as an object
# Upload the file object to sql database

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(on_file_received3, content_types=['document'])
