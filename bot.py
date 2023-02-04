import logging

from aiogram.utils import executor
from aiogram import types

from handlers import start, show_amount_users, show_anime_top, help
from router import dp
# from database.db import db_connect

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
   # await db_connect()
    print('\nSTART\n')

    await dp.bot.set_my_commands([
    types.BotCommand("top_anime", "Показать топ аниме"),
    types.BotCommand("help", "Навигация"),
    ])

start.register_handlers_start(dp)
show_amount_users.register_handlers_show_amount_user(dp)
show_anime_top.register_handlers_show_anime_top(dp)
help.register_handlers_help(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
