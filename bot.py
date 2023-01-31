import logging

from aiogram.utils import executor
from aiogram import Bot, Dispatcher, types

from handlers import start, show_amount_users, show_anime_top
from router import dp
from database.db import db_connect

logging.basicConfig(level=logging.INFO)

TOKEN = '5893032007:AAHJI8qP1Jd6uL_bskWOLZfVdiLI1L1r2A8'

# Пнг приветствия
PHOTO = 'https://avatanplus.com/files/resources/original/58f1ea455683515b70fb1eea.png'

# Мой chat_id
admin_chat_id = 1050726426


async def on_startup(_):
    await db_connect()
    # print('\nSTART\n')

start.register_handlers_start(dp)
show_amount_users.register_handlers_show_amount_user(dp)
show_anime_top.register_handlers_show_anime_top(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)








