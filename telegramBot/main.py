import asyncio
import logging
import os
import dill
import logging
import pandas as pd
from datetime import datetime
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from telegramBot.config import API_TOKEN
from aiogram.utils import executor
from telegramBot.config import URL_APP
from telegramBot.handlers import client, other, admin
from telegramBot.dataBase import dataBase as db


logging.basicConfig(level=logging.ERROR)

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


def predict(df):
    features = df.drop('price', axis=1)
    with open('model.pickle', 'rb') as f:
        model = dill.load(f)
    predictions = model.predict(features)
    df['Predictions'] = predictions
    df['Difference'] = df['price'] - df['Predictions']
    return df


# the function should also use the criteria specified by each user
def suggestProperties():
    df_str = str(db.get_new_properties())
    col_str = str(db.get_column_names())
    logging.critical(f'\n DF: {df_str} \n COL: {col_str}')
    df = pd.DataFrame(db.get_new_properties(), columns=db.get_column_names(), index='index')
    logging.critical(str(df))
    if not df:
        logging.critical('DF IS EMPTY')
    df = predict(df)
    positiveRows = df.loc[df['Difference'] > 0]
    return positiveRows['link'].values.tolist()


# the admin will use this command to notify the users manually after he changed added a df with new properties
async def notify():
    subscribers = db.get_subscriptions()
    for subscriber in subscribers:
        propertiesSuggested = suggestProperties()
        for property in propertiesSuggested:
            await bot.send_message(subscriber[0], property)


    # async def notify(interval):
    #     while True:
    #         now = datetime.utcnow()
    #         subscribers = db.get_subscriptions()
    #         for subscriber in subscribers:
    #             await bot.send_message(subscriber[0], f"{now}")
    #         await asyncio.sleep(interval)


async def on_startup(dp):
    print('Bot is online')
    await bot.set_webhook(URL_APP)
    # asyncio.create_task(notify(6))


async def on_shutdown(dp):
    await bot.delete_webhook()
    db.close()

client.register_handlers_client(dp)
other.register_handlers_other(dp)
admin.register_handlers_client(dp)


executor.start_webhook(
    dispatcher=dp,
    webhook_path='',
    on_startup=on_startup,
    on_shutdown=on_shutdown,
    skip_updates=True,
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 500))
)