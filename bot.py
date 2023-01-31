import logging

from aiogram.utils import executor

from handlers import start, show_amount_users, show_anime_top
from router import dp
from database.db import db_connect

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    await db_connect()
    # print('\nSTART\n')

start.register_handlers_start(dp)
show_amount_users.register_handlers_show_amount_user(dp)
show_anime_top.register_handlers_show_anime_top(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)








