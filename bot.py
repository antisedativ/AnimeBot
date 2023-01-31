import logging

from aiogram import executor
from router import dp
from handlers import start, show_amount_users, show_top
from message_text import GREETINGS


# from database.db import (
#     db_connect,
#     db_add_user,
#     db_show_users,
#     db_close,
#     db_show_count_users
# )


async def on_startup(_):
    print('start')

start.register_handlers_start(dp)
show_amount_users.register_handlers_show_amount_user(dp)
show_top.register_handlers_show_top(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)
